from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel
from json import JSONEncoder
import json
import uvicorn
from mysql.connector import connect, Error

app = FastAPI()


@app.post('/barbecue')
def put_babrbecue():
    query_str = "SELECT * FROM barbecue;"
    return transform_date_barbecue(execute_select_query(query_str))


def transform_date_barbecue(date):
    return date


@app.post('/contacts')
def put_contacts():
    query_str = "SELECT * FROM Contacts;"
    return transform_date_contacts(execute_select_query(query_str))


def transform_date_contacts(date):
    return date


@app.post('/sheepmeat')
def put_bakery():
    query_str = "SELECT * FROM sheepmeat;"
    return transform_date_sheepmeat(execute_select_query(query_str))


def transform_date_sheepmeat(date):
    return date


@app.post('/beef')
def put_beef():
    query_str = "SELECT * FROM beef;"
    return transform_date_beef(execute_select_query(query_str))


def transform_date_beef(date):
    return date


def execute_select_query(query: str):
    # try:
    with connect(
            host="localhost",
            user='root',
            password='qwerty123',
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


if __name__ == '__main__':
    print("Проверка")
    uvicorn.run('main:app', port=1234, host='127.0.0.1', reload=True)