import pyodbc

connection= pyodbc.connect('Driver={sql server};'+
                           'server=ADMINISTRATOR;'+
                           'database=sql demo;'+
                           'Trusted_connection=True')

print('connected to data base')

# Creating a cursor object to interact with the database
cursor = connection.cursor()

# SQL query to create the table
cursor.execute('''
CREATE TABLE employees3 ( 
    employee_id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    department VARCHAR(50),
    salary INT
                           
);
''')

cursor.execute('''
INSERT INTO employees3 (employee_id, name, department, salary)
VALUES 
    (1, 'enosh', 'sales', 5000),
    (2, 'priya', 'IT', 7000),
    (3, 'kiran', 'big data', 8500),
    (4, 'sakshi', 'billing', 4500)
;
''')

# Commit changes and close the cursor
connection.commit()

# Print success message
print('Connected to database table created and inserted successfully')

# Close the connection
cursor.close()
connection.close()






