#A program that reads a 5-digit number displays the digits of the number at intervals.
# ی# برنامه ای که یک عدد 5 رقمی را خواند ، ارقام عدد را بافاصله نمایش می دهد.
num=int(input("Enter you Number 5 digit?"))
a1= num % 10
temp = num // 10
a2 = temp % 10
temp = temp // 10
a3 = temp % 10
temp = temp // 10
a4 = temp % 10
temp = temp // 10
a5 = temp % 10
temp = temp // 10
print(a5," ",a4," ",a3," ",a2," ",a1)