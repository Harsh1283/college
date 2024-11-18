import mysql.connector
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harsh",
    database="quiz_db"
)
cursor = db.cursor()

def setup_database():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(50) NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        question TEXT NOT NULL,
        option1 VARCHAR(50),
        option2 VARCHAR(50),
        option3 VARCHAR(50),
        option4 VARCHAR(50),
        answer VARCHAR(50)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        score INT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

def insert_questions():
    questions = [
        ("What does SQL stand for?", "Structured Query Language", "Structured Question Language", "Simple Query Language", "None of the above", "Structured Query Language"),
        ("Which SQL statement is used to extract data from a database?", "GET", "EXTRACT", "SELECT", "OPEN", "SELECT"),
        ("Which SQL clause is used to sort the result-set?", "ORDER BY", "SORT BY", "GROUP BY", "ARRANGE BY", "ORDER BY"),
        ("Which command is used to delete a table in SQL?", "DELETE TABLE", "REMOVE TABLE", "DROP TABLE", "CLEAR TABLE", "DROP TABLE"),
        ("What does the WHERE clause do?", "Limits the data", "Specifies conditions", "Joins tables", "Sorts data", "Specifies conditions"),
        ("What is a primary key?", "A unique identifier", "A duplicate identifier", "A foreign key", "None of the above", "A unique identifier"),
        ("Which keyword is used to retrieve unique values?", "UNIQUE", "DISTINCT", "UNLIKE", "SPECIFIC", "DISTINCT"),
        ("What is a foreign key?", "A field linking to a primary key in another table", "A field with unique values", "A key that locks tables", "None of the above", "A field linking to a primary key in another table"),
        ("What is normalization?", "Removing redundancy", "Adding redundancy", "Deleting tables", "Creating indexes", "Removing redundancy"),
        ("Which SQL function is used to count the number of rows?", "SUM()", "COUNT()", "TOTAL()", "NUMBER()", "COUNT()"),
        ("In which normal form is a table if it has no transitive dependency?", "1NF", "2NF", "3NF", "BCNF", "3NF"),
        ("What is a JOIN in SQL?", "Combining columns from multiple tables", "Combining rows from multiple tables", "Grouping rows", "Sorting tables", "Combining rows from multiple tables"),
        ("Which SQL statement is used to insert new data into a table?", "INSERT INTO", "ADD INTO", "PUT INTO", "UPDATE INTO", "INSERT INTO"),
        ("What is the purpose of the GROUP BY clause?", "To group identical values", "To delete duplicates", "To count rows", "To limit rows", "To group identical values"),
        ("Which SQL function is used to get the maximum value?", "MIN()", "TOP()", "MAX()", "UPPER()", "MAX()"),
        ("What is a composite key?", "A key that is a combination of two or more columns", "A key with unique values", "A primary key", "None of the above", "A key that is a combination of two or more columns"),
        ("What is a candidate key?", "A primary key", "A key that could be a primary key", "A foreign key", "None of the above", "A key that could be a primary key"),
        ("What is the purpose of the HAVING clause?", "To filter groups based on conditions", "To limit rows", "To sort results", "To join tables", "To filter groups based on conditions"),
        ("What does ACID stand for in databases?", "Add, Create, Implement, Delete", "Atomicity, Consistency, Isolation, Durability", "Aggregate, Consistency, Isolation, Data", "None of the above", "Atomicity, Consistency, Isolation, Durability"),
        ("What is a view in SQL?", "A virtual table", "A copy of a table", "A stored procedure", "A backup of a table", "A virtual table")
    ]
    insert_query = """
    INSERT INTO questions (question, option1, option2, option3, option4, answer)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, questions)
    db.commit()
    print("20 questions have been inserted successfully into the questions table.")

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()
    print("Registration successful! Please log in to continue.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    if user:
        print("Login successful!")
        return user[0]
    else:
        print("Invalid username or password.")
        return None

def get_random_questions():
    cursor.execute("SELECT * FROM questions ORDER BY RAND() LIMIT 5")
    return cursor.fetchall()

def take_quiz(user_id):
    questions = get_random_questions()
    score = 0
    for q in questions:
        print("\n" + q[1])
        print(f"A. {q[2]}")
        print(f"B. {q[3]}")
        print(f"C. {q[4]}")
        print(f"D. {q[5]}")
        answer = input("Your answer (A/B/C/D): ").lower()
        if answer == 'a' and q[2] == q[6]:
            score += 1
        elif answer == 'b' and q[3] == q[6]:
            score += 1
        elif answer == 'c' and q[4] == q[6]:
            score += 1
        elif answer == 'd' and q[5] == q[6]:
            score += 1
    cursor.execute("INSERT INTO scores (user_id, score) VALUES (%s, %s)", (user_id, score))
    db.commit()
    print(f"\nQuiz completed! Your score is {score}/5.")

def main():
    setup_database()
    insert_questions()
    while True:
        print("\n1. Register\n2. Login\n3. Quit")
        choice = input("Select an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            user_id = login()
            if user_id:
                take_quiz(user_id)
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

cursor.close()
db.close()
