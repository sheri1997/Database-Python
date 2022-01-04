from fastapi import FastAPI
from pydantic import BaseModel
from DatabaseConnection import DataBase
from Queries import Queries

# class Fastapi(BaseModel):
app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Welcome to the fast api Program"}
#
#
# @app.get("/name")
# def user():
#     return {"Name": "Shreesh"}

database = DataBase.connection_database()
cursor = database.cursor(buffered=None)


class Fastapi(BaseModel):
    id: int
    first_name: str
    last_name: str

    @app.get('/')
    def root(self):
        return {"message": "Welcome to the fast api Program"}

    @app.get('/all')
    def get_first_name(self):
        data = Queries.retrieve()
        val = [i for i in data]
        return val

    @app.post('/add')
    def add_user(self):
        data = Queries.add("Azc", "PPP", "9995555", "hgvyv@bhb.com", "UP", "Azamgarh")
        return data


