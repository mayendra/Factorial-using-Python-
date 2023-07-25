"""By Mayendra Dwika Prayudha"""

#recurtion 
while True:
    n=int(input(" Type a number : "))
    def factorial(n):
        if n==1:
            return 1
        else:
            return n*factorial(n-1)
        
    print("The factorial {} is ".format(n))
    print(factorial(n))
        
        
   
        