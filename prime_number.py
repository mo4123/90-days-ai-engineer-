n=int(input("Enter the number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("It's a prime number")
else:
    print("It's not a prime number")