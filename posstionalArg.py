"""=========================================================================
						1. Posstional Arguments
			=========================================================================
=>Posstional Arguments Mechanism is the default passing arguments  mechanism used by PVM in Functions for Passing the values of Arguments 
of Function Call to Formal Parameters of Function Defintion.
=>Possitional Arguments concept says that Every Argument  Value Passing to Every  Formal Parameter Based on their Posstion by maintaining 
Order and Meaning for Higher Accuracy. In Otherwords The number of arguments must be equal to Number of Formal Parameters.
=>Possitional Arguments concept always used for Passing Specific Data from Function calls to Function Definitions.
 =>PVM gives High Priority for Possitional Arguments
---------------------------------
Syntax:     def  functionname(Param1,Param2,....Param-n):  # Function Definition
			-----------------------------------------------
			-----------------------------------------------
			Block of Statements--perform Operation
			------------------------------------------------
			-----------------------------------------------
-------------
Syntax:       functioname(arg1,arg2,.....,arg-n)  # Function call
-------------
=>Here the values of arg1,arg2,.....,arg-n of  Function call are passing to Param1,Param2,....Param-n of Function Definition Respectively.
===============================================x=========="""






def add(a,b,c):
	d=0
	d=a+b+c
	return d



print(add(10,20,30))


#positinal args/ kyeword args

def pos(name,department):
	name=print(f"hello {name}")
	department=print(f"im in branch of  {department} student")


# print(pos(department="cs",name="sanch"))# kyeword args
print(pos("sanch","cs"))#first valu is first para and second value is second para that whay this is called positonal args

#mixing of positional and keyword args
print(pos("sanch",department="cs"))#this is also called positonal args we can not write fist kyeword args and second positonal args it will give error



#default agrumment
def defluagg(name,city="bam"):
	name=print(f"hello {name}")
	city=print(f"im from {city}")

print(defluagg("bunty"))

#variable length agrgs or opssinal arbitary args it called


def varlen(*args): # arbitrary args in possitional args
	for i in args:
		print(i)

print(varlen(10,20,30,40,50))
print(varlen(10,20,30,40,50,60,70,100))
print(varlen(10,20,30,40,50,60,-70,80,130,-40,150))

#keyword length args or arbitary keyword args

def keylen(**kwargs):
	for i,j in kwargs.items():
		print(i,j)


print(keylen(name="sanch",age=20,city="bam"))
print(keylen(name="sanch",age=20,city="bam",roll=12))
print(keylen(name="sanch",age=20,city="bam",roll=12,marks=90))


def pos(name,department):
	name=print(f"hello {name}")
	department=print(f"you are in {department}")

print(pos("sanch",department="cs"))#this is also called positonal args we can not write fist kyeword args and second positonal args it will give error
