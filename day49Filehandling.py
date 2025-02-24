

#write mode if the file doesnot exits then it creates the file
'''
file=open("abc.txt",'w')
file=open("day49.txt",'w')
'''


'''
#write something in write mode
file=open("day49.txt",'w')

# print(file)

temp=file.write("yahhhhoooooooooooo.....")
temp=file.write("hellow ,welcome in day49 \n" "today we learn about file handling in python \n")

temp=file.write("read mode='r'\n""write mode='w' \n" "append mode='a' ")
print(temp)
file.close()
'''



'''
#file reading mode

file=open("day49.txt",'r')

temp=file.read()
print(temp)
file.close()
'''
'''
#append mode in python

file = open('day49.txt', 'a')
file.write("This will add this line..example of appened")
file.close()
'''

#realine by line...its read only first line
file = open('day49.txt', 'r')
line=file.readline()
print(line)

#for read multiple lines

file = open('day49.txt', 'r')
while True:
    line=file.readline()
    if not line:
        break    
    print(line)