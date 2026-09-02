Name=input("Enter your name: ")
subject_1=int(input("Enter the marks of subject 1: "))
subject_2=int(input("Enter the marks of subject 2: "))
subject_3=int(input("Enter the marks of subject 3: "))
subject_4=int(input("Enter the marks of subject 4: "))
subject_5=int(input("Enter the marks of subject 5: "))

total = subject_1+subject_2+subject_3+subject_4+subject_5

average = total/5

print("Average Marks:", average)

if total>=450:
    print("Grade: A")
elif total>=400:
    print("Grade: B")
elif total>=350:
    print("Grade: C")


print("Name:", Name)
print("Total Marks:", total)

