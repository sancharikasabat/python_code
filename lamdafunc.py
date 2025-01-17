'''--------------------------------------------------------------------------------------------------------------------------------------------
Syntax:		varname = lambda params-list : Expression
------------------------------------------------------------------------------------------------------------------------------------------------------------------
=>here varname Represents an Object of type <class,'function'>. So that we use that Varname as Function Call
=>here lambda is keyword used for Define Anonymous Functions
=>here params-list Represents List of Variables used for Storing the Input(s) coming From Functions.
=>Expression represents single Executable statement and Provides Solution for tiny Problems a dn whose Result 
    Returns automatuically (No Need to use return statement).
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
			Question: Define a Function for addition of two Numbers
***************************************************************************************************************************************************
		Normal Function						Anonymous Function
	--------------------------------------				------------------------------------------------------------
def  sumop(a,b):							addop = lambda a,b : a+b
	return (a+b)

#Main Program							#Main Program
res=sumop(10,20)							res=addop(4,5) # Anonymous Function Call
print("sum=",res)							print("sum=",res)
====================================================================================='''

#wtp wich will accept 2 values find wuch one is biggest them .using anonymous fun

findmax=lambda a,b:max(a,b) # also use the min 

#main
a=int(input("enter the first value"))
b=int(input("enter the second value"))

print(findmax(a,b))

print("============or============")
#i want to print max min and also both are same

varname=lambda a,b:a if a>b else b if b>a else "both r same"
a=int(input("enter the first value"))
b=int(input("enter the second value"))

#main

# print(varname(a,b))

print("=============or===================")

