import pyodbc

connection= pyodbc.connect('Driver={sql server};'+
                           'Server=ADMINISTRATOR;'+
                           'Database=sql demo;'+
                           'Trusted_connection=True')

cursor=connection.cursor()


cursor.execute('''Insert into  employees3  (employee_id,name,department,salary)
                values(5,'riya','non-tech',3500);''')

cursor.commit()
print('record added sucessfully')

cursor.close()


 
 
