list1=[]
sum1=0
avg=0
count=0
while True :
    
    number=int(input("Enter Number : "))
    if number <=0 :
        break
    if number not in list1:
        list1.append(number)
    sum1+=number
    count+=1
        
               
 
avg=sum1/count
print("sum : ",sum1)
print("avg : ",avg)
print(list1)