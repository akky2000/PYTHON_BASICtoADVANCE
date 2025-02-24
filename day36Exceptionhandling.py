#HANDLE THE DIFFERENT TYPE OF ERROR
'''
try:
   #statement
except:
      #statement
'''

'''
a=int(input("enter the number:"))
print(f"multiplication table of {a}")
try:
    for i in range(1,11):
        print(f"{int(a)}X{i}= {int(a)*i}")
except ValueError :
 print("invalid input plz enter valid input")

print("kya haal chal hai")
'''


'''
try:
    num=int(input("enter an input:"))
except:
    print("number entered is not an integer")
'''




'''
def div(a,b):
    temp=a/b
    print(temp)
print(div(1,0))  #ZeroDivisionError: division by zero
#handled ny try except
'''

def divide(a,b):
    try:
        temp=a/b
        print(temp)
    except:
        print("invalid input")
print(divide(0,0))
