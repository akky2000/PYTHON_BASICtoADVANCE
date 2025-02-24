#   LISTS IN PYTHON

l1=[1,2,3,4,"akky",True,2.3]
print(l1)



#accesing
print(l1[3])

#negative indexing
print(l1[-5])

#check whether an item is present in list?
colors=["red", "yellow", "green"]
if "blue" in colors:
    print("yes")
else:
    print("no")



marks=[11,22,44,55,66,77,88]
print (marks)
print(len(marks))

print(marks[2])

print(marks[:])
print(marks[2:6])
print(marks[2:-3])




#LIST COMPREHENSION

l1=[i for i in range(4)]
print(l1)

l2=[i for i in range(10) if i%2==0]
print(l2)