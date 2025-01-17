"""
The Process of Converting One Possible Type Value into another Type of Value is called Type Casting.
In Python Programming, we have 5 Fundamental Type Casting Techniques. They are 
            1.int()
			2. float()
			3. bool()
			4. complex()
			5. str()

"""
print("==================int=======================")
#str to int
ex1="10"
print(type(ex1))
ex2=int(ex1)
print(type(ex2))

#str to float
ex3="10.5"
print(type(ex3))
ex4=float(ex3)
print(type(ex4))

#str to bool
ex5="True"
print(type(ex5))
ex6=bool(ex5)
print(type(ex6))

#str to complex
ex7="10+5j" 
print(type(ex7))
ex8=complex(ex7)
print(type(ex8))

print("==================float=======================")


ex9=10.3
print(type(ex9))
print(int(ex9))
print(ex9)

ex10=10
print(type(ex10))
print(float(ex10))
print(ex10)

ex11=10.5
print(type(ex11))
print(bool(ex11))
print(ex11)

ex12=10
print(type(ex12))
print(complex(ex12))
print(ex12)


print("==================bool=======================")

ex13=True
print(type(ex13))
print(int(ex13))


ex14=False
print(type(ex14))
print(float(ex14))


ex15=True
print(type(ex15))
print(str(ex15))


ex16=False
print(type(ex16))
print(complex(ex16))


print("==================complex=======================")
"""ex=10+5j
print(type(ex)) # type error
print(int(ex))


ex17=10+5j
print(type(ex17)) 
print(float(ex17))
"""

ex18=10+5j  
print(type(ex18))
a=print(str(ex18))
print(a,type(ex18))

print("--------")

ex19=10+5j
print(type(ex19))
b=print(bool(ex19))
print(b,type(ex19))
































