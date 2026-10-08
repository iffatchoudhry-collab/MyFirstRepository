def factorial(number):
    #base condition
    if number==0 or number==1:
        return 1
    #Recursive Return
    else:
        return number*factorial(number-1)
##Test Example

n=int(input("Please enter a Number to calculate Factorial "))
print("The Factorial for ",n,"is: ",factorial(n))