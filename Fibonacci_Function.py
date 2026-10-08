def fibonacci(n,x=0,y=1,result=None):
    if result is None:
        result=[]
    if n<=0:
        return result
    
    

    result.append(x)
    return fibonacci(n-1,x=y,y=x+y,result=result)
        
       

    

#Test Example
count=int(input("Please enter a number for Fibonacci Sequence "))
#fibonacci(count)
print("The Fibonacci Sequence upto",count,"is:",fibonacci(count))
