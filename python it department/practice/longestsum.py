arr1 = [-5,3,-2,-7,5,-7,-3,-1,4,3]
arr2 = [5,2,6,3,9,7,5,2,9]
arr3 = [-3,-4,-2,4,5,-6,-1,-2,4,-6,-7,8]
total_sum=0
running_sum=0
max_length=0
current_length=0


for i in arr1:
    if i<0:
        running_sum+=i
        current_length+=1
      
        if current_length>max_length:
            max_length=current_length
            total_sum=running_sum
        elif current_length==max_length:
            total_sum+=running_sum
    else:
        running_sum=0
        current_length=0
if total_sum==0:
    print("-1")
else:
    print(total_sum)                
         
        
