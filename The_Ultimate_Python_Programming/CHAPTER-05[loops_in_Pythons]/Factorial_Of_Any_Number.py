n = int(input("Enter any number:"))
fact = 1
#i = 1
#while i<=n:
for n in range(1,n+1):
    fact = fact*n
print("The factorial of",n,"is :",fact)