import psycopg2

# Database connection parameters
HOST = "localhost"  # Change this if needed
DBNAME = "postgres"  # Your PostgreSQL database name
USER = "postgres"  # Your PostgreSQL username
PASSWORD = "Praveen@123"  # Your PostgreSQL password

# Function to establish a connection to the PostgreSQL database
def connect_db():
    return psycopg2.connect(
        dbname=DBNAME, user=USER, password=PASSWORD, host=HOST
    )

# Create the students table if it doesn't exist
def create_table():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    );
    """)

    connection.commit()
    print("Students table created successfully")

    cursor.close()
    connection.close()

# Create a new student
def create_student(name, age, email):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO students (name, age, email) VALUES (%s, %s, %s)", (name, age, email))
    connection.commit()
    print(f"Student {name} added successfully")

    cursor.close()
    connection.close()

# Read all students
def read_students():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Email: {student[3]}")

    cursor.close()
    connection.close()

# Update a student's details
def update_student(student_id, name=None, age=None, email=None):
    connection = connect_db()
    cursor = connection.cursor()

    if name:
        cursor.execute("UPDATE students SET name = %s WHERE id = %s", (name, student_id))
    if age:
        cursor.execute("UPDATE students SET age = %s WHERE id = %s", (age, student_id))
    if email:
        cursor.execute("UPDATE students SET email = %s WHERE id = %s", (email, student_id))

    connection.commit()
    print(f"Student with ID {student_id} updated successfully")

    cursor.close()
    connection.close()

# Delete a student by ID
def delete_student(student_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    connection.commit()
    print(f"Student with ID {student_id} deleted successfully")

    cursor.close()
    connection.close()

# Example usage
if __name__ == "__main__":
    # Create the table (if not exists)
    create_table()

    # Add some students
    create_student("Alan walker", 21, "alan@walker.com")
    create_student("june slith", 22, "june@slith.com")
    
    # Read and display all students
    print("Students in database:")
    read_students()

    # Update a student's information
    update_student(1, name="Johnathan Doe", age=22)

    # Delete a student
    delete_student(2)

    # Read and display students after update and delete
    print("Students after update and delete:")
    read_students()
