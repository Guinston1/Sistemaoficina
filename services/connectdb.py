import mysql.connector
import os
from mysql.connector import Error
from dotenv import load_dotenv
from pathlib import Path


def connectdb():

    env_path = Path(__file__).parent / "db.env"
    load_dotenv(env_path)

    load_dotenv("db.env")

    DB_CONFIG = {
        "host":     os.getenv("DB_HOST"),
        "user":     os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME")
    }

    print(DB_CONFIG)
    print("DB_HOST:", os.getenv("DB_HOST"))
    print("DB_USER:", os.getenv("DB_USER"))
    print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
    print("DB_NAME:", os.getenv("DB_NAME"))
    print(DB_CONFIG)

    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("successful connection")

    except Error as err:
        print(f"Error: '{err}'")

    return connection

