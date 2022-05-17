grade = int(input("Enter grade: "))
if (0 <= grade <= 70):
    print("Fail")
elif 71 <= grade <= 80:
    print("Good")
elif 81 <= grade <= 90:
    print("Very good")
elif 91 <= grade <= 100:
    print("Excellent")
else:
    print("Invalid grade")