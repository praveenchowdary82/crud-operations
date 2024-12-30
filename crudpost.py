import psycopg2

# Database connection parameters
HOST = "localhost"
DBNAME = "postgres"
USER = "postgres"
PASSWORD = "Praveen@123"

# Establish a connection to the PostgreSQL database
def connect_db():
    return psycopg2.connect(
        dbname=DBNAME, user=USER, password=PASSWORD, host=HOST
    )

# Create a table
def create_table():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE
        )
    """)
    connection.commit()
    print("Table created successfully")
    cursor.close()
    connection.close()

# Create a user
def create_user(name, email):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    connection.commit()
    print(f"User {name} created successfully")
    cursor.close()
    connection.close()

# Read users
def read_users():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    cursor.close()
    connection.close()

# Update a user
def update_user(user_id, name=None, email=None):
    connection = connect_db()
    cursor = connection.cursor()
    if name:
        cursor.execute("UPDATE users SET name = %s WHERE id = %s", (name, user_id))
    if email:
        cursor.execute("UPDATE users SET email = %s WHERE id = %s", (email, user_id))
    connection.commit()
    print(f"User with ID {user_id} updated successfully")
    cursor.close()
    connection.close()

# Delete a user
def delete_user(user_id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    connection.commit()
    print(f"User with ID {user_id} deleted successfully")
    cursor.close()
    connection.close()

# Example usage:
if __name__ == "__main__":
    # Create the table
    create_table()

    # Create some users
    create_user("Alice", "alice@example.com")
    create_user("Bob", "bob@example.com")
    
    # Read and display users
    print("Users in database:")
    read_users()

    # Update a user
    update_user(1, name="Alicia", email="alicia@example.com")

    # Delete a user
    delete_user(2)

    # Read and display users after update and delete
    print("Users after update and delete:")
    read_users()
