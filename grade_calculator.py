mark = int(input("enter your mark:"))
if mark>=90 and mark<=100:
    print("Grade A")
elif mark>100:
    print("Invalid mark enter the correct mark")
elif mark>=80 and mark<90:
    print("Grade B")
elif mark>=70 and mark<80:
    print("Grade C")
elif mark>=50 and mark<70:
    print("Grade D")
elif mark<50:
    print("Fail")
