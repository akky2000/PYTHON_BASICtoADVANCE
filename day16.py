#MATCH STATEMENT IN PYTHON  SAME AS SWITCH STATEMENT IN C,C++ETC

a=int(input('enter the value betwwen 1 and 3:'))

match a:
    case 0:
        print("number is three")
    case 1:
        print("number is one ")
    case 2:
        print("number is two ")
    case _:
        print("number is not between 1 and 3")









# x=int(input('enter the value'))

# match x:
#     case x if x<0:
#         print("number is negative")
#     case x if x>0:
#         print("number is positive")
#     case _:
#         print("number is zero")