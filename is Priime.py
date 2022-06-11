n = int(input("Enter Your Number : ?"))
isPrime = True 
for i in (2, n // 2+ 1):
    if n % i == 0:
        isPrime = False
    break
if (isPrime==True):
    print("Yes")
else:
    print("No")
