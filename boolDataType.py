""" 

'bool' is one of the Pre-Defined Class and treated as Fundamental Data Type.
=>The bool data type is used for Storing  True and False Values.
=>Here True and False are Keywords and They are treated as boolean values.
=>Programtically, the True is Internally Treated as 1 and False treated as 0.
=>On bool values we can Arithmetic Operations (Called Boolean Arithmetic )

"""


a=True
print(a,type(a))

b=True
c=True
ex1=(b+c)
print(ex1)

ex2=True+True
print("ex2=",ex2)


ex3= False + False
print(ex3)

ex4=False +True
print(ex4)

print("-------------minus------------------")

ex5=True-True
print("ex5=",ex5)


ex6= False - False
print(ex6)

ex7=False - True
print(ex7)

x=True-False
print(x)

print("--------------divaide-----------------")

ex8=True / True
print("ex8=",ex8)


# ex8= False / False
# print(ex8)

ex8=False / True
print(ex8)

# y=True / False 
# 
# #ZeroDivisionError: division by zero