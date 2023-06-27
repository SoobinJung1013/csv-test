import pymysql
from config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME

def connect_database():
    conn = pymysql.connect(
        host=DATABASE_HOST,
        port=3306,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )
    return conn
