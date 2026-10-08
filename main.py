# Team Name: The Equals SQLs
# Student Numbers: 4351723,...
# File Name: main.py

from db_config import get_db_connection

def main():
    conn = get_db_connection()
    if conn:
        print("Database connection verified. Ready for queries.")
        conn.close()

if __name__ == "__main__":
    main()