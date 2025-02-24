#FUNCTION : IT IS VERY IMPORTANT IN PYTHON 


#create a function to add two number
'''

def AddNum(a,b):    #creating a function one time and use many times in program
    temp=a+b
    print(temp)

AddNum(3,5)
AddNum(10,11)

'''

#create a functio for sub , multiply ,division for two number

#subtraction
'''def SubNum(a,b):
    temp1=a-b
    print(temp1)

SubNum(5,3)
SubNum(4,5)
'''


#multiply
'''
def MulNum(a,b):
    temp2=a*b
    print(temp2)

MulNum(22,3)
MulNum(22,10)
'''

#divide
'''
def DivNum(a,b):
    temp3=a/b
    print(int(temp3))

DivNum(10,2)
DivNum(5,2)
'''












'''
Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
'''

def MulNums(*numbers):
    print(type(numbers))
    temp=1
    for i in numbers:
       temp=temp*i
    print("ans is:",temp )
MulNums(8,2,3,-1,7)