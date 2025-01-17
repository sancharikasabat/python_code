"""
a+bj  OR   a-bj

			Here 'a' is called Real Part
			Here 'b' is called Imaginary Part
			and The letter 'j' Represents sqrt(-1 )  OR sqr(j) = -1
=>Here the Real and Imarinary part of Complex Number are Treated Internally as float type.
=>To get Real and Imaginary Parts, we have Two Pre-Defined Attributes Present in Complex Object. They are
			
				1. real
				2. imag
		Syntax:   complexobj.real  ------>Gives Real part of complex object
				complexobj.imag ------>Gives Imaginary part of complex object
"""

ex1= 3+4j
print(ex1.real)
print(ex1.imag)

ex2= 3-4j
print(ex2.real)
print(ex2.imag)

ex3= 3j
print(ex3.real)
print(ex3.imag)

ex4= -3j
print(ex4.real)
print(ex4.imag)

ex5= 3+0j
print(ex5.real)
print(ex5.imag)

ex6= -3-5j
print(ex6.real)
print(ex6.imag)

ex7= 3.4+9.3j
print(ex7.real)
print(ex7.imag)

ex8= 3.4-9.3j
print(ex8.real)
print(ex8.imag)

ex9= 3.4j
print(ex9.real)
print(ex9.imag)

ex10= -3.4j
print(ex10.real)
print(ex10.imag)


ex13= 4+1j
ex14= 3-0j
print("pluse:",ex13+ex14)
print("minus:",ex13-ex14)
print("multiply:",ex13*ex14)
print("divide:",ex13/ex14)

ex11= 3.4+0j
ex12= -3.4-0j
print("pluse:",ex11+ex12)
print("minus:",ex11-ex12)
print("multiply:",ex11*ex12)
print("divide:",ex11/ex12)
#print(ex1%ex2) #unsupported operand type(s) for %: 'complex' and 'complex'

