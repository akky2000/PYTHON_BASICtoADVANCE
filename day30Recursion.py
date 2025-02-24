#RECURSION 

'''
factorial number means
f(0)=1
f(1)=2
f(2)=2*1
f(3)=3*2*1
f(4)=4*3*2*1
f(5)=5*4*3*2*1
'''


def Factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return (n*Factorial(n-1))
print(Factorial(3))
print(Factorial(4))
print(Factorial(5))


#fibonacci series
'''
f(0)=0
f(1)=1
f(2)=f(1)+f(0)
f(n)=f(n-1)+f(n-2)
'''

def fibonacci(n):
    if(n==0):
        return 0
    if(n==1 or n==2):
        return 1

    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    

temp = 20

print("Fibonacci series:")
for i in range(0, temp + 1):
    print(fibonacci(i), end=" ")
        



    