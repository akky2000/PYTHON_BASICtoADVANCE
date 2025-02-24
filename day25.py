#TUPLES METHOD IN PYTHON
#manipulating the tuples


tup1=(1,2,3,4,"red")
temp=list(tup1)  #convert tuples into a list
temp.append("blue")
temp.pop(2)
temp[2]="yellow"
tup1=tuple(temp)
print(tup1)


print(tup1.count(2))
print(tup1.index(1))