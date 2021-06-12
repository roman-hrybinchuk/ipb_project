from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import hashlib


def hash_password(password: str):
    return hashlib.md5(password.encode('utf-8')).hexdigest()


def verify_password(hashed_password: str, plain: str):
    return hashed_password == hash_password(plain)


def is_email_exist(db: Session, email: str) -> bool:
    res = db.query(models.Person).filter(models.Person.email == email).first()

    return res is not None


def create_manager(db: Session, manager: schemas.ManagerCreate):
    db_manager = models.Manager(email=manager.email, hashed_password=hash_password(manager.password))
    db.add(db_manager)
    db.commit()
    db.refresh(db_manager)
    return db_manager


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(email=employee.email, hashed_password=hash_password(employee.password))
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(passport_id=user.passport_id, email=user.email, hashed_password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def login_user(db: Session, email: str, password: str) -> models.Person:
    user = db.query(models.Person).filter(models.Person.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    if not verify_password(user.hashed_password, password):
        raise HTTPException(status_code=401, detail="Bad password")

    return user


def get_user_loans(db: Session, user_id: int) -> List[models.Loan]:
    loans = db.query(models.Loan).filter(models.Loan.user_id == user_id).all()
    print(f'Loans {loans}')
    return loans


def get_pending_requests(db: Session) -> List[models.LoanRequest]:
    requests = db.query(models.LoanRequest).filter(models.LoanRequest.status == 'pending').all()
    return requests


def update_loan_status(db: Session, new_status: str, loan_id: int, manager_id: int) -> models.LoanRequest:
    request: models.LoanRequest = db.query(models.LoanRequest).filter(models.LoanRequest.id == loan_id).first()

    if not request:
        raise HTTPException(status_code=404, detail="Not found")

    request.status = new_status

    request.reviewer_id = manager_id

    db.add(request)
    db.commit()
    db.refresh(request)

    return request


def get_loan_requests(db: Session, user_id: int) -> List[models.LoanRequest]:
    data = db.query(models.LoanRequest).filter(models.LoanRequest.user_id == user_id).all()

    return data


def create_loan_request(db: Session, request_create: schemas.LoanRequestCreate) -> models.LoanRequest:
    active = db.query(models.Loan).filter(models.Loan.id == request_create.user_id,
                                          models.Loan.status == 'active').first()

    if active:
        raise HTTPException(status_code=400, detail="You need to close old loan")

    request_exists = db.query(models.LoanRequest).filter(models.LoanRequest.status == 'pending').first()

    if request_exists:
        raise HTTPException(status_code=400, detail="You have pending request")

    db_loan_request = models.LoanRequest(**request_create.dict())

    db.add(db_loan_request)
    db.commit()
    db.refresh(db_loan_request)

    return db_loan_request


def create_loan(db: Session, loan: schemas.LoanCreate):
    request: models.LoanRequest = db.query(models.LoanRequest).filter(models.LoanRequest.user_id == loan.user_id,
                                                                      models.LoanRequest.amount == loan.amount).first()

    if not request:
        raise HTTPException(status_code=400, detail="Something is wrong")

    request.status = 'archived'

    db.add(request)
    db.commit()

    loan = models.Loan(**loan.dict())

    db.add(loan)
    db.commit()
    db.refresh(loan)

    return loan
