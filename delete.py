import pyodbc

connection= pyodbc.connect('Driver={sql server};'+
                           'Server=ADMINISTRATOR;'+
                           'Database=sql demo;'+
                           'Trusted_connection=True')
cursor=connection.cursor()

cursor.execute('Delete from employees3 where employee_id=5')
cursor.commit()
print('Record deleted sucessfully')
cursor.close()