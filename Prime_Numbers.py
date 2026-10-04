while True:
 num=int(input("Enter a number upto which to Print all prime numbers: "))
 if num<2:
   print("Enter a number greater than 2 ")
 else:
   break
prime=[]
for number in range(2,num+1):
  check=True
  for i in range(2,int(number**0.5)+1):
    if number%i==0:
      check=False
      break
  if check:
      prime.append(number)

print("Prime Numbers upto ",num,"are: ",prime)
                
    




