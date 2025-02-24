#ifstatement

# a=10
# b=22
# if(a<b):
#     print("b is greater than a")

#     #if-else

#     age=int(input("enter your age:"))
#     if(age>=18):
#         print("you can derive")
#     else:
#         print("u cant derive")



# elif condition


# num=int(input("enter the number:"))
# if(num<0):
#     print("number is negative")

# elif(num==0):
#     print("number is zero")

# else:
#     print("number is positive")

# print("i am happy")



# nested if

num=int(input("enter  a number :"))
if(num<0):
    print("number is negative")
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num>10 and num<=20):
        print("number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")





