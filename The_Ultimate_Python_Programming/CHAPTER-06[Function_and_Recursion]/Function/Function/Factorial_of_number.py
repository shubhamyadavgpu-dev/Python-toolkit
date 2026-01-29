
#num = int(input("Enter a number to find its factorial: "))
#def fact(num) :
#    if num == 0 :
 #       return 1
 #   else :
 #       return num * fact(num - 1)
#print(fact(num))
n = 5
fact = 1
def fact(num) :
    for i in range(1,n+1) :
            fact = fact*i
    return fact   
print(fact(5))         