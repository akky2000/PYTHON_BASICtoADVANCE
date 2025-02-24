#local variable vs global variable in python




'''
x=4

def hello():
    y=3
    print(y)
hello()
print(f"global variable is{x}")

# print(y) # local variable is not accesible outside the function
'''


x=4

def hello():
    global x
    x=233
    y=3
    print(y)
hello()
print(f"global variable is{x}")