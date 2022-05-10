#1. برنامه ای که یک عدد دورقمی را خواند ، مقلوب آن را نمهایش هی دهد )ههد برنامهه - 
a = input("Enter a number: ")
a = int(a)
r1 = a % 10
print(r1)
r2 = a // 10
print(r2)
print ("Reverse is ", r1 * 10 + r2)