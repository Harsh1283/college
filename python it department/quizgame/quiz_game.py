
user_data={}
def register():
    username=input("enter your username:")
    password=input("enter your password:")
    
    user_data[username]=password
         
         
    with open("data.txt","w") as file:
         for key, value in user_data.items():
              a=(f"{key}: {value}")
              print(a)
        
              file.write(a)

    
    


 
def login():
     username=input("enter your username:")
     password=input("enter your password:")
   
     cred=f"{username}: {password}"
     
     with open("data.txt","r") as file:
        for line in file:
          
            if line.strip()==cred:
                print("login succesfully")
                break
               
            else:
                print("username invalid")
    
       
from main import run_quiz,questions
             
def main():
    a=(input("1 for register\n2 for login \n3 for exit :"))
    print(a)
    if '1'==a:
        register()
    elif '2'==a:
        login()
        if "login succesfully"=="login succesfully":
            run_quiz(questions)
           
    else:
        print("exiting")
         
      
      
      
main()      