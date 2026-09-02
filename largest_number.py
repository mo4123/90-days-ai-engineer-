a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter another number: "))
if a>b and a>c:
    print("The largest number is:", a)
elif b>a and b>c:
    print("B is greater",b)
else:
    print("C is greater",c)