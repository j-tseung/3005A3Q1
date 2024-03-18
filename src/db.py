# /src/db.py
import psycopg2
from psycopg2.extras import RealDictCursor
import os

def connect_db():
    try:
        return psycopg2.connect(
            dbname='A3Q1',
            user='postgres',
            password='postgres',
            host='localhost',
            cursor_factory=RealDictCursor  # Allows to fetch rows as dictionaries
        )
    except Exception as e:
        print(f"Database connection failed due to {e}")
