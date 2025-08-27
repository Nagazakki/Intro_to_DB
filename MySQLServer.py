import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host = 'localhost'
            user = 'root'
            password = '@Holaputa5'
        )
            
        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            connection.commit()
            print("Database 'alx_book_store' created successfully.")
    
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    except mysql.connector.Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

def main():
    print("Attempting to create MySQL database...")
    create_database()

if __name__ == "__main__":
    main()