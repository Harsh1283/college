import mysql.connector

connection=mysql.connector.connect(
    host='localhost',
    user="root",
    password="mandu",
    database="mandu"
)


cursor=connection.cursor()


create_table_query="""
CREATE TABLE STUDENT(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100),
    AGE INT,
    GRADE VARCHAR(10)
);
"""


insert_data_student="INSERT INTO STUDENT (name,age,grade) VALUES(%s,%s,%s);"
values=("hars",22,'A')
cursor.execute(insert_data_student,values)



#cursor.execute(create_table_query)

select_query="SELECT * FROM STUDENT;"
cursor.execute(select_query)
results=cursor.fetchall()

connection.commit()

print("data added")




for row in results:
    print(row)

# if connection.is_connected():
#     print("maja aagaya")

cursor.close()
connection.close()