#برنامه ای که عدد رو از ورودی بگیره و اعداد مربع تا اون عدد رو محاسبه کنه 
# ابتدا تابع برای مربع تا عدد مورد نظر رو مینویسیم و بعد درون بذنه برنامه ورودی رو میکیریم و بعد مقایسه میکنیم اگر true  بود 
# اوکی مربع هست .
def issquare(n):
    i = 1
    while i * i <= n:
        if (i * i == n):
            return True
        i = i + 1
    return False

n = int(input("enter a number: "))
for i in range (1,n+1):
    if issquare(i) == True:
        print(i, end="\t")
