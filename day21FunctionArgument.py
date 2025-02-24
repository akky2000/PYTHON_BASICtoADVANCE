#ARGUMENTS:four type arguments of function

# #default arguments

# def add(a=2,b=3):
#     temp=a+b
#     print (temp)
# add()
# add(9)
# add(3,4)


# def sub(c,d):
#     temp=c-d
#     print(temp)

# sub(2,2)

'''

def avg(*numbers):
    sum=0
    for i in numbers:
        sum= sum+i
        print("average :", sum/len(numbers))

avg(2,4)
'''


def add(*numbers):
    temp=0
    for i in numbers:
        temp=temp+i
    print("addition:",temp)

add(1,2,5)


def add(*numbers):
    temp=0
    for i in numbers:
        temp=temp+i
    # print("addition:",temp)
    return temp

c=add(1,2,5,6,7,8)
print(c)