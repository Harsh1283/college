a=float(input("write your no. :"))
b=float(input("write your second no. :"))
c=input("what you want to do : \n(1.multiplication \n 2.addition \n 3.subtraction \n 4.division \n) -->")
if '1'==c:
    print("multiplication of",a,"*",b,a*b)
elif '2'==c:
     print("addition of",a,"+",b,a+b)
elif '3'==c:
     print("subtraction of",a,"-",b,a-b)  
elif '4'==c:
    if b!=0:
        print("error")
    else:
        print(a/b)    
else:
    print("invalid input")        
   