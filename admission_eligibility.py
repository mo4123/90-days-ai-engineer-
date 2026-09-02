name=input("enter your name:")
age=int(input("enter your age:"))
percentage=int(input("enter your percentage:"))
entrance= int(input("enter your entrance exam mark:"))

if age>=17 and percentage>=60 and entrance>=50:
    print("Student:",name)
    print("Admission Status: Eligible")
elif age<17:
    print("Admission Status: Not Eligible")
    print("your age is less than 17")
elif percentage<60:
    print("Admission Status: Not Eligible")
    print("your percentage is less than 60")
elif entrance<50:
    print("Admission Status: Not Eligible")
    print("your entrance is less than 50")
