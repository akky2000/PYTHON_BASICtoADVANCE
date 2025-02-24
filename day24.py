#tuples in python

tup1=(1,2,3,4,5,7,8,"green",4.3,True)
# tup1[1]=20    #tuples are not changable after tuples are create 
print(tup1)
print(type(tup1))
print(tup1[0])
print(tup1[7])
print(tup1[1:-1])

#chech the element is vaailable in tuples
if "green" in tup1:
    print("yes it is available")
else:
    print("no")


print(tup1[1:-1:2]) #jump statement,jumped by 2



