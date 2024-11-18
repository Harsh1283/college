# from quiz_game import register
import mysql.connector

connection=mysql.connector.connect(
    host='localhost',
    user="root",
    password="harsh",
    database="harsh"
)


cursor=connection.cursor()

# storing_user="""
# CREATE TABLE USER(
#     ID INT AUTO_INCREMENT PRIMARY KEY,
#     USERNAME VARCHAR(20),
#     PASSWORD VARCHAR(20)
    
# );
# """


insert_data="INSERT INTO USER(USERNAME,PASSWORD) VALUES(%s,%s);"
values=(register.username,register.password)

cursor.execute(insert_data)

connection.commit()

print("table created")

cursor.close()
connection.close()
