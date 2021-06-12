import pkg_resources
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
security = HTTPBasic()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    manager_email = "manager@my.email"
    manager_password = "123"

    employee_email = "employee@my.email"
    employee_password = "123"

    try:
        manager = schemas.ManagerCreate(email=manager_email, password=manager_password)
        crud.create_manager(db, manager)

        employee = schemas.EmployeeCreate(email=employee_email, password=employee_password)
        crud.create_employee(db, employee)
        print('Created')
    except Exception as e:
        print(e)


@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = crud.login_user(db, credentials.username, credentials.password)
    return {'user': user}


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print('here')
    if crud.is_email_exist(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    print('res')
    return crud.create_user(db=db, user=user)


@app.post("/requests/manager/{request_id}")
def get_loans_manager(request_id: str, new_status: str, credentials: HTTPBasicCredentials = Depends(security),
                      db: Session = Depends(get_db)):
    user = crud.login_user(db, credentials.username, credentials.password)

    requests = crud.update_loan_status(db, new_status=new_status, loan_id=request_id, manager_id=user.id)

    return {'requests': requests}


@app.get("/requests/manager")
def get_loans_manager(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    crud.login_user(db, credentials.username, credentials.password)

    requests = crud.get_pending_requests(db)

    return {'requests': requests}


@app.get("/requests/employee/{user_email}")
def get_loans_by_user_email(user_email: str, credentials: HTTPBasicCredentials = Depends(security),
                            db: Session = Depends(get_db)):
    crud.login_user(db, credentials.username, credentials.password)

    user = db.query(models.User).filter(models.User.email == user_email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    requests = crud.get_loan_requests(db, user.id)

    return {'requests': requests}


@app.get("/loans")
def get_loans(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = crud.login_user(db, credentials.username, credentials.password)
    loans = crud.get_user_loans(db, user.id)
    return {'loans': loans}


@app.post("/loans")
def create_loan(loan: schemas.LoanCreate, credentials: HTTPBasicCredentials = Depends(security),
                db: Session = Depends(get_db)):
    crud.login_user(db, credentials.username, credentials.password)

    loan = crud.create_loan(db, loan)

    return {'loan': loan}


@app.get("/loan_request")
def user_loans(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = crud.login_user(db, credentials.username, credentials.password)

    loan_requests = crud.get_loan_requests(db, user.id)
    return {'loan_requests': loan_requests}


@app.post("/loan_request")
def create_loan_request(amount: int, credentials: HTTPBasicCredentials = Depends(security),
                        db: Session = Depends(get_db)):
    user = crud.login_user(db, credentials.username, credentials.password)

    data = schemas.LoanRequestCreate(amount=amount, user_id=user.id)

    loan_request = crud.create_loan_request(db, data)

    return {'loan_request': loan_request}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
