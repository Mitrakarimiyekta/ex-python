s = input("Enter a string:")
count = 0
for i in s :
    if '0' <= i <= '9':
        count = count + i
print("Count is ", count)
