'''
index


=>Arguments and Parameters
=>Types of Arguments and Parameters
		a) Possitional Arguments and Parameters
		b) Default Arguments and Parameters
		c) Keyword Arguments and Parameters
		d) Variable Length Arguments and Parameters
		e) Keyword Variable Length Arguments and Parameterms
=>Programming Examples
---------------------------------------------------------------------------------------------
=>Local and Global Variables
=>Programming Examples
=>global Keyword
=>Programming Examples 
=>globals() concept
=>Programming Examples
---------------------------------------------------------------------------------------------
=>Comprehension Concept
		a) List Comprehension
		b) set Comprehension
		c) dict Comprehension
		d) tuple Comprehension (Not there)
=>Programming Examples
---------------------------------------------------------------------------------------------
=>Anonymous OR Lambda Functions
=>Implementation of Anonymous OR Lambda Functions
=>Programming Examples
---------------------------------------------------------------------------------------------
=>Special Functions in Python
		a) filter() with Normal and Anonymous Functions
		b) map() with Normal and Anonymous Functions
		c) reduce() with Normal and Anonymous Functions
=>Programming Examples
========================================x==================================================










				Functions in Python
===========================================================
=>The purpose of Functions is that " To Perform Certain Operation /Task and Provides Code Re-Usability".
=>The Advantages of Functions in any languages are
			1. Application Development time is Less
			2. Application Memory Space is Less
			3. Application Execution Time is Less
			4. Application Performance  is Enhanced
			5. Redundency of the Code is Minimized
--------------------------------------------------------------------------------------------------------------------------------
Definitions of Function
--------------------------------------------------------------------------------------------------------------------------------
=>Sub Program of Main Program is Called Function.
			(OR).
=>A Part of main program is Called Function.
--------------------------------------------------------------------------------------------------------------------------------
Parts of Functions
--------------------------------------------------------------------------------------------------------------------------------
=>At the time Developing functions in real time, we must ensure that, there must exist 2 Parts. they are
		1. Function Definition
		2. Function Calls
=>Every Function Definition Exists Only Once
=>Every Function call must contains a Function Defintion Otherwise we get NameError.
=>Function Definition will execute when we call by using function calls OR Without  calling the 
    Function by using Function Calls, PVM will not execute Function Definition.
--------------------------------------------------------------------------------------------------------------------------------
Phases in Functions
--------------------------------------------------------------------------------------------------------------------------------
=>At the time Defining the functions, the Programmer must ensure that there must exist the following Phases.
		1. Every Function Must take INPUT
		2. Every Function Must PROCESS the Input
		3. Every Function Must give OUTPUT or RESULT

		
-----------------------------------------------------------------------------------------



'''

def add (a,b):#formal parameter
    c=a+b
    print(c)

x=int(input("enter the value of a:"))
y=int(input("enter the value of b:"))
# add(x,y)   #argument actual parameter 



def dev (p,q):
   k= p-q
   print(k)

# dev(x,y)


def mul (r,s):
    j=r*s
    print(j)

mul(x,y)


print('==============================default parameter===========================')

 
