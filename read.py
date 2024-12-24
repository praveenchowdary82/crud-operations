import pyodbc

connection= pyodbc.connect('Driver={sql server};'+
                           'server=ADMINISTRATOR;'+
                           'database=sql demo;'+
                           'Trusted_connection=True')

cursor=connection.cursor()
try:
    cursor.execute('select * from employees3')
    result =cursor.fetchall()
    for i in result:
        employee_id=i[0]
        name=i[1]
        department=i[2]
        salary=i[3]
        print(employee_id,name,department,salary)
except:
    print('some issue in the code')

    cursor.close()
    