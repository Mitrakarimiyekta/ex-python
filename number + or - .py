#برنامه ای که عددی را خواند ، تشخیص می دهد، مثبت، صفر یا منفی است
number=int(input("Enter Your Number: "))
if number < 0:
    print("Number is negative")
elif number == 0:
    print("Number is zero,")
else:
    print("Number is positive,")