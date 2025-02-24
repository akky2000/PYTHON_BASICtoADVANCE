'''
s1={10,20,30}
s2={30,40,50}


#union method and update method
print(s1.union(s2))
(s1.update(s2))

print(s1,s2)
print(s1 | s2)
'''



'''
#intersection method
print(s1.intersection(s2))
print(s1 & s2)

print(s1 ^ s2)

'''


'''
#SYMMETRIC DIFFERENCE METHOD
set1={"red","blue","white"}
set2={"green","red","yellow"}

print(set1.symmetric_difference(set2))
print(set1.symmetric_difference_update(set2))
'''

'''
#DIFFERENCE METHOD
set1={10,40,20,30}
set2={30,10}
print(set1.difference(set2))
print(set1.difference_update(set2))
print(set1)
'''


#pop METHOD
'''
s1={11,22,33,44}
s1.pop()  
print(s1)
'''

#remove method
'''
s2={12,13,14,15}
s2.remove(13)
print(s2)
'''

#clear method
'''
s1={11,12,13}
s1.clear()
print(s1)
'''


#discard method
'''
s1={20,30,40,50}
s1.discard(20)
print(s1)
'''

#issuperjoint

s1={22,33,44}
s2={22,33,44}

s3=s1.issuperset(s2)
print(s3)


s4=s2.issubset(s1)
print(s4)


s5=s1.isdisjoint(s2)
print(s5)

