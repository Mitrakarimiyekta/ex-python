#برنامه ای که مشخص کند عدد ورودی داده شدهاول هست یا کامل 
#عددی اول هست که مجموع مقسوم علیه های عدد برابر باشه با 1
#عددی تام یا کامل هست که مجموع مقسوم علیه های عدد با خودش برابر باشد 




#اولین تابعی که مینویسم برای جمه مقسوم علیه ها هست 
def sumdivided(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum = sum + i
    return sum

def isperfect(n):
    if sumdivided(n) == n:
        return True

def isprimary(n):
    return sumdivided(n) == 1

n=int(input("enter a number: "))
if isperfect(n) == True:
    print("perfect number")
elif isprimary(n) == True:
    print("primary number")
else:
    print("not primary or perfect number")
