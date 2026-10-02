while True:
 count=int(input("How many Fibonacci numbers will you like to Print? "))
 ##check if user eneterd positive number
 if count<=0:
  print("Please enter positive number ")
  print("")
 else:
    break
x=0
y=1

print("Fibonacci sequence up to", count,": ")
while count>0:
        print(x, end=" ")
        z=x+y
        x=y
        y=z
        count-=1