#LAMBDA FUNCTION IN PYTHON

#normal function
def add(x,y):
    return x+y
print(add(3,4))


#now we using lambdaFunction
add=lambda x,y:x+y
print(add(3,5))


def cube(x):
    return x*x*x
print(cube(10))

cube=lambda x:x*x*x
print(cube(3))