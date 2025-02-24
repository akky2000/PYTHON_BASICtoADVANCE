#FOR LOOP IN PYTHON


fruits=["apple","mango","banana","orange"]
for fruit in fruits:    #print fruit name in fruits
    print(fruit)
    if(fruit=="banana"):
        continue

    # for i in fruit:
    #     print(i)




name="AKASH"
for i in name:   #print character by character of name 
    print(i)



#range()function
for s in range(5,30,5):
    if s==20:
        break
    print(s)
else:
    print("happy")    




#nested loop in python

names=["ram","shyam","rohan","sohan"]
fruitss=["apple","banana","orange","mango"]

for x in names:
    for y in fruitss:
        print(x,y)

for s in [1,2,3]:
    pass
    


