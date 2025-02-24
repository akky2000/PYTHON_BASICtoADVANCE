#DICTIONARIES IN PYTHON


d1={'name':'akash', 'age':22,'eligible':True}
print(d1)
print(type(d1))


#accessing single value
info={'name':'rahul', 'age':22,'eligible':True}
print(info['name'])
print(info.get('name'))


employe_id={
    331:"akash",
    223:"mayank",
    3:"chandu"
}
print(employe_id[3])

#accessing multiple values

print(info.values())