#map function, filter function , reduce function
# def cube(x):
#     return x*x*x
# print(cube(2))

l=[1,2,3,4,5]

'''
newL=[]
for item in l:
    newL.append(cube(item))
print(newL)
  '''


#by using MAP funtion how it looks
# newL=list(map(cube,l))
# print(newL) 

#using lambda function with map
# newL=list(map(lambda x:x*x*x,l))
# print(newL) 



#FILTER FUNCTION.....
'''
def filter_function(a):
    return a>4
temp=list(filter(filter_function,l))
print(temp)
'''



#REDUCE FUNCTION
from functools import reduce
#work with same l=[1,2,3,4,5]
sum =reduce(lambda x,y:x+y,l)
print(sum)