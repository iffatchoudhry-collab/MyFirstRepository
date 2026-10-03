n=int(input("Please enter a number to find Factorial for: "))
fact=1
if n<0:
    print("Please enter positive Integer ")
elif n==0:
    print("The factorial of 0 is 1 ")
else: 
    for number in range(1,n+1):
        fact*=number
    

print("The factorial of ",n,"is :",fact)