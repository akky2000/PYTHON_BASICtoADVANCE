#STRING METHOD


name="Akash"
nnn="AKASH"
nm=len(name)
print(nm)
print(name.upper())#upper case


print(name.lower())  #lower case



#rstrip

a="Akash!!!!"
print(a.rstrip("!"))

#replace 
print(a.replace("Akash","raj"))


b="akash kumar kashyap"
print(b.split(" "))



# capitalize

c="introduction tO python programming"
print(c.capitalize())

#center
str1="welcome to  my world"
print(str1.center(30))
print(len(str1.center(30)))

#count()

print(str1.count("o"))


#endwith()
str2="how r uhh !!!"
print(str2.endswith("!!!"))
print(str2.endswith("#"))

print(str2.endswith("r",2,5))


#find() SAME AS INDEX()

str3="welcome to my world"
print(str3.find("my"))
print(str3.find("hellow"))

print(str3.find("l"))

# print(str3.index("hellow"))  #ERRORSHOW

#isalnum()

str4="welcomebro"
print(str4.isalnum())

str5="wwee00"
print(str5.isalpha())

#islower()

print(str4.islower())

#isprintable()
str6="hellow my name is akash"
print(str6.isprintable())

str7="hellow my name is akash\n"
print(str7.isprintable())
print(str7.title())









