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
CREATE TABLE student (
    name VARCHAR(30) NOT NULL,
    marks INT
);
''')

# Commit changes and close the cursor
connection.commit()

# Print success message
print('Connected to database and table created successfully')

# Close the connection
cursor.close()
connection.close()


# use sql demo;
