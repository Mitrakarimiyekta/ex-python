n = int(input("Enter n:"))
p = 1
for i in range(n, 0, -1):
    print(i, end = '\t')
    p = p * i
print("\nMultiply iss :", p)