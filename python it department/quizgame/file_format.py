import json

data=[
     {
        "questions": "What is the output of the following code: print(type([]))?",
        "options": ["A) <class 'list'>", "B) <class 'dict'>", "C) <class 'tuple'>", "D) <class 'set'>"],
        "answer": "A"
    },
    {
        "questions": "Which of the following is the correct syntax to create a function in Python?",
        "options": ["A) function myFunction()", "B) def myFunction():", "C) create myFunction()", "D) func myFunction():"],
        "answer": "B"
    },
    {
        "questions": "What is the result of 3 * 1 ** 3?",
        "options": ["A) 3", "B) 1", "C) 9", "D) 27"],
        "answer": "A"
    },
    {
        "questions": "How do you insert a comment in Python?",
        "options": ["A) // This is a comment", "B) # This is a comment", "C) /* This is a comment */", "D) <!-- This is a comment -->"],
        "answer": "B"
    },
    {
        "questions": "Which method can be used to remove any whitespace from both the beginning and the end of a string?",
        "options": ["A) strip()", "B) trim()", "C) len()", "D) slice()"],
        "answer": "A"
    },
    {
        "questions": "What is the output of the following code: print(2 == 2 == 1)?",
        "options": ["A) True", "B) False", "C) 1", "D) 0"],
        "answer": "B"
    },
    {
        "questions": "Which of the following is not a valid variable name in Python?",
        "options": ["A) my_var", "B) 2ndVar", "C) var_2", "D) _myVar"],
        "answer": "B"
    },
    {
        "questions": "What will be the output of this code: print(bool(0))?",
        "options": ["A) True", "B) False", "C) None", "D) Error"],
        "answer": "B"
    },
    {
        "questions": "Which of the following data types is immutable in Python?",
        "options": ["A) List", "B) Set", "C) Dictionary", "D) Tuple"],
        "answer": "D"
    },
    {
        "questions": "What does the len() function do?",
        "options": ["A) Returns the length of an object", "B) Returns the first element of an object", "C) Returns the type of an object", "D) Returns the last element of an object"],
        "answer": "A"
    },
    {
        "questions": "Which keyword is used to handle exceptions in Python?",
        "options": ["A) try", "B) catch", "C) handle", "D) except"],
        "answer": "A"
    },
    {
        "questions": "What is the purpose of the pass statement in Python?",
        "options": ["A) To pass control to the next iteration", "B) To indicate that nothing happens", "C) To exit a loop", "D) To skip the next statement"],
        "answer": "B"
    },
    {
        "questions": "How do you create a list in Python?",
        "options": ["A) list[]", "B) []", "C) list()", "D) new list()"],
        "answer": "B"
    },
    {
        "questions": "What will be the output of this code: print({1, 2, 2, 3})?",
        "options": ["A) {1, 2, 3}", "B) {1, 2, 2, 3}", "C) [1, 2, 3]", "D) Error"],
        "answer": "A"
    },
    {
        "questions": "What is the correct way to import a module in Python?",
        "options": ["A) import module", "B) include module", "C) require module", "D) using module"],
        "answer": "A"
    },
    {
        "questions": "Which function can be used to convert a string to an integer?",
        "options": ["A) int()", "B) str()", "C) float()", "D) char()"],
        "answer": "A"
    },
    {
       "questions": "What is the output of the following code: print('Hello'[1])?",
        "options": ["A) H", "B) e", "C) l", "D) o"],
        "answer": "B"
    },
    {
        "questions": "Which of the following is used for formatting strings in Python?",
        "options": ["A) %", "B) .format()", "C) f-strings", "D) All of the above"],
        "answer": "D"
    },
    {
        "questions": "What is a lambda function in Python?",
        "options": ["A) A function that returns a value", "B) A function defined with 'lambda' keyword", "C) A function that can take any number of arguments", "D) None of the above"],
        "answer": "B"
    },
    {
        "questions": "How do you check if a key exists in a dictionary?",
        "options": ["A) key in dict", "B) dict.has_key(key)", "C) key in dict.keys()", "D) All of the above"],
        "answer": "D"
    }
]



with open('json.txt','w') as file:
    json.dump(data,file)
    
with open("json.txt",'r') as file:
    data=json.load(file)    
    
   
#for q in data:
 #   print(q["questions"])  
  #  for options in q["options"]:
   #     print(options)
        
        
        
        
def run_quiz(data):
    score = 0
    for q in data:
        print(q["questions"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").upper()

        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Your final score is: {score}/{len(data)}")      
    
    
run_quiz(data)      
    