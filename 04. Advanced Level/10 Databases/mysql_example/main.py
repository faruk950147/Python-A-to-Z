import mysql.connector

try:
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="python_db"
    )
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Create a database
    cursor.execute("CREATE DATABASE IF NOT EXISTS python_db")
    
    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE,
            email VARCHAR(255) NOT NULL UNIQUE,
            roll INT NOT NULL UNIQUE,
            country VARCHAR(255) NULL
        )
    """)

    # Insert data
    cursor.execute("""
        INSERT IGNORE INTO users (name, email, roll, country)
        VALUES 
            ('Faruk', 'faruk@example.com', 101, 'Bangladesh'),
            ('Ahmed', 'ahmed@example.com', 102, 'Bangladesh'),
            ('Jay', 'jay@example.com', 103, 'India'),
            ('Mina', 'mina@example.com', 104, 'India'),
            ('Charlie Brown', 'charlie@example.com', 105, 'Germany'),
            ('Diana Prince', 'diana@example.com', 106, 'France'),
            ('Eve Wilson', 'eve@example.com', 107, 'Japan')
    """)

    # Commit the transaction
    conn.commit()
    print("Data inserted successfully!")
    
    # Query data
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

except (mysql.connector.Error, Exception) as err:
    print("Error occurred:", err)
