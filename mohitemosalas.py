#برنامه ای که سه ضلع مثلث راخوانده محیط و مساحت مثلث را بدست بیاورد 

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter b: "))
p = (a + b + c )
print("Perime is ", p)
p = p / 2
s=(p * (p - a )*(p - b) *(p -c))**0.5
print("Area is ", s)