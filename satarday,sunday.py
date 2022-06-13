n=int(input("ٍEnter Yoyr Number :"))
n = n % 7
if n == 0:
    print("SatarDay")
elif n==1:
    print("sunday")
elif n == 2:
    print("monday")
elif n == 3:
    print("tuesday")
elif n == 4:
    print("wednsday")
elif n == 5:
    print("tuersday")
elif n == 6:
    print("friday")
else:
    print("invalid number")
    