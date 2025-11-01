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
    
    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE,
            email VARCHAR(255) NOT NULL UNIQUE,
            roll INT NOT NULL UNIQUE
        )
    """)

    # Insert data
    cursor.execute("""
        INSERT IGNORE INTO users (name, email, roll)
        VALUES 
            ('John Doe', 'john@example.com', 101),
            ('Jane Doe', 'jane@example.com', 102),
            ('Bob Smith', 'bob@example.com', 103),
            ('Alice Johnson', 'alice@example.com', 104)
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
