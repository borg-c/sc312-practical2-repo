# Team Name: The Equal SQLs
# File Name: db_config.py

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'your_database_name')
        )
        if connection.is_connected():
            print("Successfully connected to MySQL database.")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        conn.close()
