Hi, welcome to my repo!

The code is in code folder, it consist from fastapi (Python) backend and vue front end and sqlite.


To get it up here is the list of instructions.


`cd code`

`virtualenv venv ` To createnv

`.\venv\Scripts\activate.ps1` Or `.\venv\Scripts\activate.bat` If you inside cmd.

`pip install -r .\requirements.txt` To install python dependencies;

The set up for backend is done you can run it by calling.

`uvicorn main:app` You should be in the venv

Now to set up front end.


`cd code/clientv2`

`yarn install`

`yarn serve` And go to the front end urls.


Then you can register ( you will be registered as default client)
Where you can apply for loan.(Please refresh page after apply and close modal -: )

But also you need to login from another browser to simulate manager and emplyoee.

Here is the logins for them.

```
    manager_email = "manager@my.email"
    manager_password = "123"

    employee_email = "employee@my.email"
    employee_password = "123"
```

Once you apply for a loan manager should get the application.

After approving it, employee will be able to search by email for client and issue money.


Please make sure than backend is running on 8080.

