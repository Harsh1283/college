import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harsh",
    database="quiz_py"
)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    score INT DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT,
    choice_a TEXT,
    choice_b TEXT,
    choice_c TEXT,
    choice_d TEXT,
    correct_answer CHAR(1)
)
""")

questions_data = [
    ('What is SQL?', 'Structured Query Language', 'System Query Language', 'Simple Query Language', 'Structured Question Language', 'A'),
    ('What is the primary key?', 'A key that uniquely identifies each record', 'A key that links tables', 'A key used for indexing', 'A key used for sorting', 'A'),
    ('What is normalization?', 'Organizing the data', 'Reducing data redundancy', 'Combining data into one table', 'Reducing the size of the data', 'B'),
    ('What is a foreign key?', 'A key that uniquely identifies each record', 'A key used to link two tables', 'A key used for indexing', 'A key used for sorting', 'B'),
    ('What is the purpose of a database index?', 'To speed up data retrieval', 'To store large amounts of data', 'To reduce the number of tables', 'To create foreign key relationships', 'A'),
    ('What is the full form of ACID in databases?', 'Atomicity, Consistency, Isolation, Durability', 'Accuracy, Consistency, Isolation, Durability', 'Atomicity, Consistency, Information, Durability', 'Atomic, Consistent, Isolated, Durable', 'A'),
    ('What is a JOIN operation in SQL?', 'Combining two tables based on a condition', 'Sorting data from two tables', 'Counting records in two tables', 'Renaming tables', 'A'),
    ('What does a SELECT statement do?', 'Inserts data into a table', 'Updates data in a table', 'Deletes data from a table', 'Retrieves data from a table', 'D'),
    ('What is a database view?', 'A virtual table', 'A table storing temporary data', 'A table that holds large data', 'A view of the data from the database', 'A'),
    ('Which of the following is a data type in SQL?', 'INT', 'FLOAT', 'VARCHAR', 'All of the above', 'D'),
    ('Which SQL keyword is used to sort the result-set?', 'SORT BY', 'ORDER BY', 'ARRANGE BY', 'ORDER', 'B'),
    ('Which of the following commands is used to add data to a table?', 'INSERT', 'ADD', 'INSERT INTO', 'ADD INTO', 'C'),
    ('What is a subquery?', 'A query inside another query', 'A complex query', 'A query that performs a calculation', 'A query that updates a table', 'A'),
    ('What is the default value for NULL in SQL?', '0', 'None', 'An empty string', 'Undefined', 'D'),
    ('What is the purpose of a GROUP BY clause?', 'To group records by a specific column', 'To filter results', 'To sort results', 'To join tables', 'A'),
    ('What is a relational database?', 'A database that stores data in tables', 'A database that stores data as JSON', 'A database that stores data as graphs', 'A database with no relationships', 'A'),
    ('What is a stored procedure?', 'A set of SQL statements that can be executed', 'A stored query', 'A stored view', 'A stored trigger', 'A'),
    ('What does the COUNT() function do?', 'Counts rows in a table', 'Sums the values of a column', 'Finds the average of a column', 'Finds the maximum value', 'A'),
    ('Which SQL command is used to modify an existing table?', 'MODIFY', 'ALTER', 'UPDATE', 'INSERT', 'B'),
    ('Which of the following is NOT a valid SQL constraint?', 'PRIMARY KEY', 'FOREIGN KEY', 'IDENTITY', 'UNIQUE', 'C')
]

cursor.executemany("""
INSERT INTO questions (question, choice_a, choice_b, choice_c, choice_d, correct_answer)
VALUES (%s, %s, %s, %s, %s, %s)""", questions_data)

conn.commit()
cursor.close()
conn.close()
print("hello")
# cursor.execute("SELECT * FROM questions ORDER BY RAND() LIMIT 5")
# random_questions = cursor.fetchall()
