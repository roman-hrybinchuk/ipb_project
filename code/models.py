import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship

from database import Base


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    type = Column(String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_on': type
    }


class User(Person):
    __tablename__ = "users"

    id = Column(ForeignKey("persons.id"), primary_key=True)

    passport_id = Column(String, unique=True)
    loanRequests = relationship("LoanRequest", back_populates="user")
    loans = relationship("Loan", back_populates="user")
    __mapper_args__ = {
        'polymorphic_identity': 'users',
    }


class Manager(Person):
    id = Column(ForeignKey("persons.id"), primary_key=True)

    __tablename__ = "managers"
    loanRequests = relationship("LoanRequest", back_populates="reviewer")

    __mapper_args__ = {
        'polymorphic_identity': 'managers',
    }


class Employee(Person):
    __tablename__ = "employees"

    id = Column(ForeignKey("persons.id"), primary_key=True)
    loanRequests = relationship("LoanRequest", back_populates="served")

    __mapper_args__ = {
        'polymorphic_identity': 'employees',
    }


class LoanRequest(Base):
    __tablename__ = "loan_requests"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default='pending')
    amount = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="loanRequests")

    reviewer_id = Column(Integer, ForeignKey("managers.id"), nullable=True)
    reviewer = relationship("Manager", back_populates="loanRequests")

    served_id = Column(Integer, ForeignKey("employees.id"), nullable=True)
    served = relationship("Employee", back_populates="loanRequests")


class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default="active")
    amount = Column(Integer)
    amount_payed = Column(Integer, default=0)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="loans")
