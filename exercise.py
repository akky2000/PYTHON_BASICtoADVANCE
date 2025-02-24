# import time

# time=int(input("enter the time:"))
# if(time<12):
#     print("GOOD MORNING, HAVE A GOOD DAY")
# elif(time>12):
#     if(time<=12 and time<16):
#         print("GOOD AFTERNOON")
#     elif(time>=16 and time<=19):
#         print("good evening")
#     elif(time>19 and time<=24):
#         print("good night")
# else:
#     print("enter valid time as a indian standard time")

import time
t = time.strftime('%H:%M:%S')


# https://docs.python.org/3/library/time.html#time.strftime


hours=int(time.strftime('%H'))
hours=int(input("enter the hour:"))

print(hours)
     
if(hours>=0 and hours<12):
        print("GOOD MORNING, HAVE A GOOD DAY")

elif(hours>=12 and hours<16):
            print("GOOD AFTERNOON")
elif(hours>=16 and hours<=19):
            print("good evening")
    
else:
     print("goodnyt")



'''

try:
    timestamp = int(input("Enter the hour (0-23): "))
    if 0 <= timestamp < 24:
        if 4 <= timestamp < 12:
            print("GOOD MORNING, HAVE A GOOD DAY")
        elif 12 <= timestamp < 16:
            print("GOOD AFTERNOON")
        elif 16 <= timestamp <= 19:
            print("GOOD EVENING")
        else:
            print("GOOD NIGHT")
    else:
        print("Please enter a valid hour between 0 and 23.")
except ValueError:
    print("Invalid input. Please enter a number.")
'''