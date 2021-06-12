from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel


class LoanBase(BaseModel):
    amount: int


class LoanCreate(LoanBase):
    user_id: int


class Loan(LoanBase):
    id: int
    user_id: int
    amount_payed: int
    status: str

    class Config:
        orm_mode = True


class LoanRequestBase(BaseModel):
    amount: str


class LoanRequestCreate(LoanRequestBase):
    user_id: int


class LoanRequest(LoanRequestBase):
    id: int
    user_id: int
    date: datetime
    status: str
    reviewer_id: Optional[int] = None
    served_id: Optional[int] = None

    class Config:
        orm_mode = True


class PersonBase(BaseModel):
    email: str


class PersonCreate(PersonBase):
    password: str


class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(PersonBase):
    passport_id: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    loanRequests: List[LoanRequest] = []
    loans: List[Loan] = []

    class Config:
        orm_mode = True


class ManagerBase(PersonBase):
    pass


class ManagerCreate(ManagerBase):
    password: str


class Manager(ManagerBase):
    id: int
    loanRequests: List[LoanRequest] = []

    class Config:
        orm_mode = True


class EmployeeBase(PersonBase):
    pass


class EmployeeCreate(EmployeeBase):
    password: str


class Employee(EmployeeBase):
    id: int
    loanRequests: List[LoanRequest] = []

    class Config:
        orm_mode = True
