import mysql.connector
import random

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harsh",
    database="quiz_py"
)
cursor = conn.cursor()


def create_tables():
    cursor.execute('''
        CREATE TABLE  users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE,
            password VARCHAR(255),
            score INT DEFAULT 0
        );
    ''')
    
    cursor.execute('''
        CREATE TABLE  questions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            question TEXT,
            answer TEXT
        );
    ''')
    conn.commit()
    
    
    
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, password))
        conn.commit()
        print("Registration successful!")
    except mysql.connector.IntegrityError:
        print("Username already exists. Please try a different username.")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s ;", (username, password))
    user = cursor.fetchone()
    
    if user:
        print("Login successful!")
        return user[0]  
    else:
        print("Login failed. Check your credentials.")
        return None    
 
 
    
def add_sample_questions():
    questions = [
        ("What is the primary key?", "A unique key that uniquely identifies each record"),
        ("What does SQL stand for?", "Structured Query Language"),
        ("What is a foreign key?", "A key used to link two tables together"),
        ("What is a join in SQL?", "An operation to combine rows from two or more tables"),
        ("What is a database?", "An organized collection of data"),
        ("Define normalization.", "A process to minimize redundancy in data"),
        ("What is a stored procedure?", "A prepared SQL code that can be saved and reused"),
        ("What is an index?", "A data structure that improves the speed of data retrieval"),
        ("Explain ACID properties.", "Atomicity, Consistency, Isolation, Durability"),
        ("What is a view?", "A virtual table based on the result of a query"),
        ("What is a transaction?", "A sequence of database operations treated as a single unit"),
        ("What is the use of the GROUP BY clause?", "To group rows that have the same values"),
        ("Explain the difference between DELETE and TRUNCATE.", "DELETE removes rows one by one; TRUNCATE removes all rows"),
        ("What is the use of the HAVING clause?", "To specify a search condition for a group or aggregate"),
        ("What is the purpose of the SQL SELECT statement?", "To fetch data from a database"),
        ("Explain the difference between UNION and UNION ALL.", "UNION removes duplicates; UNION ALL includes all duplicates"),
        ("What is an ER diagram?", "A graphical representation of entities and relationships"),
        ("What is the purpose of the DISTINCT keyword?", "To return unique values"),
        ("Define a candidate key.", "A key that can uniquely identify a record in a table"),
        ("What is a schema?", "The structure of a database defined by tables, fields, and relationships")
    ]
    
    cursor.executemany("INSERT INTO questions (question, answer) VALUES (%s, %s)", questions)
    conn.commit()
    print("Sample questions added!")
    
    
def fetch_random_questions():
    cursor.execute("SELECT * FROM questions ORDER BY RAND() LIMIT 5")
    return cursor.fetchall()    
    
def start_quiz(user_id):
    questions = fetch_random_questions()
    score = 0
    
    for idx, (q_id, question, answer) in enumerate(questions, start=1):
        print(f"Q{idx}: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer.strip().lower() == answer.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    
    print(f"Your score: {score}/{len(questions)}")
    
    # Update score in users table
    cursor.execute("UPDATE users SET score = %s WHERE id = %s", (score, user_id))
    conn.commit()
    print("Score saved!")

def main():
    #2create_tables()
    add_sample_questions()
    
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        register()
    elif choice == '2':
        user_id = login()
        if user_id:
            start_quiz(user_id)
    else:
        print("Invalid choice. Please select 1 or 2.")
        
        
main()                