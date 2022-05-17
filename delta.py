a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
c=int(input("Enter a number :"))
delta=b**2-a*a*c
if delta < 0:
    print("Not Root")
elif delta==0:
    print(" x1 = x2 = ", -b/ (2.0 * a))
else:
    print(" x1 = ", (-b + delta ** 0.5) / (2.0 * a))
    print(" x2 = ", (-b - delta ** 0.5) / (2.0 * a))
