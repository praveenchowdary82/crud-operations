import psycopg2

conn=psycopg2.connect(host="localhost",database="postgres",user="postgres",
                      password="Praveen@123",port=5432)

cursor=conn.cursor()

cursor.execute("""create table persons (
    id int primary key,
    name varchar(100),
    age int ,
    gender varchar(50)
);
 """ )

cursor.execute("""insert into persons(id,name,age,gender) values
(1,'jessica',45,'F'),
(2,'micheal',30,'M'),
(3,'Donna',42,'F'),
(4,'harvey',55,'M')
 """)
cursor.execute("""select * from persons where age>40""")

for row in cursor.fetchall():
    print(row)

conn.commit()
cursor.close()
conn.close()