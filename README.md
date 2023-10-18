## Trying hands on Python framework - FastAPI

### Initial steps

create a requirements.txt
- > python3 -m virtualenv env
- > cd env
- > source bin/activate
- > pip3 install -r requirements.txt


## starting with api

- We need schema to start with so - schemas.py

- uvicorn product.main:app --reload

- configuration code in database.py

- Starter script of database.py from [https://fastapi.tiangolo.com/tutorial/sql-databases/]

Installing Table Plus to view the Product Database


Authentication added

- python-hose package for generating JWT

- Generate a secret key:
- > openssl rand -hex 32
