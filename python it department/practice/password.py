passw=input("enter your password:")
if 8 > len(passw) < 20:
    passw
else:
    print("your password is too long")  
    
    
lower=0
upper=0
digit=0
special=0

    
for i in passw:
    if i.isalpha():
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
    elif i.isdigit():
        digit+=1
    elif i in ["@","#","%"]:
        print("your password should not contain these '@''#''%' special character")
        exit()
    else:
        special+=1
if upper==0 or lower==0 or digit==0 or special==0:
    print("password atleast contain uppercase lowercase digit")  
else:
    print(passw,"is valid")             
                       
         
