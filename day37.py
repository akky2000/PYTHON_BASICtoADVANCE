#raising a custom error with the help of "raise" keyword


salary=int(input("enter salary amount:"))

if (salary<2000 or salary>5000):
    raise ValueError("salary amount is not valid")



age=int(input("enter your age"))

if(age<18 or age>30):
    raise ValueError("u r not eligible for exam")