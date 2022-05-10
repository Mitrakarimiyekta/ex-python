#برنامه ای که سن را دریافت کند و انرا به ساعت و دقیقه و ثانیه محاسبه کند .. هر سال برابر است با
# 3.156*10**7 
#و هر ساعت برابر است با 60 دقیقه 
#و هر ساعت برابر است با 3600 ثانیه 
#و هر دقیقه برابر است با 60 ثانیه 
age=input("Enter You age :")
age=int(age)
second=age*3156e4
minutes=second/60
hours=minutes/3600
print("second is :", second)
print(" minutes is :", minutes)
print("hourse is :", hours)