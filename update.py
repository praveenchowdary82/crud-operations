import pyodbc

connection = pyodbc.connect('Driver={sql server};'+
                            'Server=ADMINISTRATOR;'+
                            'Database=sql demo;'+
                            'Trusted_connection=True')

cursor=connection.cursor()

try:
    cursor.execute('update employees3 set salary=6500 where employee_id=2')

    cursor.commit()
    print('record updated successfully')

except:
    cursor.rollback()
