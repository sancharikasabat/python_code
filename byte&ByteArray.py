'''
			=============================================================
						2. bytes
			=============================================================
=>'bytes' is one of the Pre-Defined Class and treated as Sequence Data Type.
=>The purpose of 'bytes' is that "To Implement End-End to Encryption / Encrypted Format / Cipher Text."
=>To Implement End-End to Encryption Process by using bytes data type, the bytes data type Organizes the Data in 
    range of  (0,256) [ It stores the Data from 0 to 255 only.]
=>The bytes data type does not contain any symbolic Notation for Organizing bytes data bcoz Python Programmer 
     does not write bytes data  directly in the Program (It is Internal convertion). But as a Python Programmer can Convert other type of Values into bytes type by using bytes().
	Syntax:  varname=bytes(Iterable-object)
=>On the Object bytes, we can perform Both Indexing and Slicing Operations
=>An Object bytes maintains Insertion order (Whatever the Order we insert OR Organize, In the same order the data 
    will be displayed )
 =>An object of bytes belongs to IMMUTABLE bcoz 'bytes' object does not support item assignment
---------------------------------------------------------------------------------------------------------------------------------------
Examples
---------------------------------------------------------------------------------------------------------------------------------------
>>> lst=[10,20,200,256,56,27]
>>> print(lst,type(lst))-----------------[10, 20, 200, 256, 56, 27] <class 'list'>
>>> b=bytes(lst)------------------------ValueError: bytes must be in range(0, 256)
>>> lst=[10,-20,200,255,56,27]
>>> print(lst,type(lst))-----------------[10, -20, 200, 255, 56, 27] <class 'list'>
>>> b=bytes(lst)-------------------------ValueError: bytes must be in range(0, 256)
--------------------------------------------------
>>> lst=[10,20,200,255,56,27]
>>> print(lst,type(lst))-----------[10, 20, 200, 255, 56, 27] <class 'list'>
>>> b=bytes(lst)
>>> print(b,type(b))--------------b'\n\x14\xc8\xff8\x1b' <class 'bytes'>
------------------------------------------------
>>> b[0]-------------------------10
>>> b[0:4]----------------------b'\n\x14\xc8\xff'
>>> for val in b[0:4]:
...		print(val)
...
			10
			20
			200
			255
>>> for val in b[::-1]:
...		print(val)
...
		27
		56
		255
		200
		20
		10
-------------------------------------------------------------
>>> lst=[10,20,200,255,56,27]
>>> print(lst,type(lst))----------------[10, 20, 200, 255, 56, 27] <class 'list'>
>>> b=bytes(lst)
>>> print(b,type(b))------------------------b'\n\x14\xc8\xff8\x1b' <class 'bytes'>
>>> b[0]-----------------10
>>> b[0]=100----------------TypeError: 'bytes' object does not support item assignment
===================================================================================


'''
print("--------------byte------------------------")
ex1=[10,20,30,40,50,60,70,80,90,100]
ex2=bytes(ex1)
print(ex2[5] , type(ex2),"\n")


print("---------for loop print bytes--------")
#using for loop print bytes
for i in ex2:
    print(i)


print("---------for loop print bytes in riverse order--------")
#print in riverse order
for i in ex2[::-1]:
    print(i)





#using index print
print("----------------using index print-----------")
for i in ex2[1:8] :
    print(i)





print("--------------bytearray------------------------\n")

"""in byte array is same the bytes but diffrent is that in can be modify
=================================================
						3. bytearray
				=================================================
=>'bytearray' is one of the Pre-Defined Class and treated as Sequence Data Type.
=>The purpose of 'bytearray' is that "To Implement End-End to Encryption / Encrypted Format / Cipher Text."
=>To Implement End-End to Encryption Process by using bytearray data type, the bytearray data type Organizes the Data in range of  (0,256) [ It stores the Data from 0 to 255 only.]
=>The bytearray data type does not contain any symbolic Notation for Organizing bytearray data bcoz Python Programmer does not write bytearray data  directly in the Program (It is Internal convertion). But as a Python Programmer can Convert other type of Values into bytearray type by using bytearray().
	Syntax:  varname=bytearray(Iterable-object)
=>On the Object bytearray, we can perform Both Indexing and Slicing Operations.
=>An Object bytearray maintains Insertion order (Whatever the Order we insert OR Organize, In the same order the data  will be displayed )
 =>An object of bytearray belongs to MUTABLE bcoz 'bytearray' object  supports item assignment either by using Indexing or by using Slicing.
===============================================================================================
NOTE: The functionality of bytearray is exactly similar to bytes. But an object of bytes belongs to IMMUTABLE where 
            as an object bytearray belongs to MUTABLE.
===============================================================================================
Examples
===============================================================================================
>>> lst=[10,20,256,56,78,100]
>>> print(lst,type(lst))---------------[10, 20, 256, 56, 78, 100] <class 'list'>
>>> ba=bytearray(lst)---------------ValueError: byte must be in range(0, 256)
>>> lst=[10,20,255,56,0,-78,100]
>>> print(lst,type(lst))--------------[10, 20, 255, 56, 0, -78, 100] <class 'list'>
>>> ba=bytearray(lst)---------------ValueError: byte must be in range(0, 256)
--------------------------------------------------
>>> lst=[10,20,255,56,0,78,100]
>>> print(lst,type(lst))-----------[10, 20, 255, 56, 0, 78, 100] <class 'list'>
>>> ba=bytearray(lst)
>>> print(ba,type(ba))------------bytearray(b'\n\x14\xff8\x00Nd') <class 'bytearray'>
>>> for val in ba:
...		print(val)
...
		10
		20
		255
		56
		0
		78
		100
>>> ba[0]--------------------------10
>>> ba[0:5]-----------------------bytearray(b'\n\x14\xff8\x00')
>>> for val in ba[0:5]:
...		print(val)
...
			10
			20
			255
			56
			0
------------------------------------------------
>>> lst=[10,20,255,56,0,78,100]
>>> print(lst,type(lst))-----------------[10, 20, 255, 56, 0, 78, 100] <class 'list'>
>>> ba=bytearray(lst)
>>> print(ba,type(ba),id(ba))----------bytearray(b'\n\x14\xff8\x00Nd') <class 'bytearray'> 1857607506160
>>> ba[-1]-----------------100
>>> ba[-1]=172 # we are updating OR replacing the value of bytearray with new value by using Indexing
>>> print(ba,type(ba),id(ba))------bytearray(b'\n\x14\xff8\x00N\xac') <class 'bytearray'> 1857607506160
>>> for val in ba:
...		print(val)
...
		10
		20
		255
		56
		0
		78
		172
>>> ba[0:2]=[122,123] # we are updating OR replacing the values of bytearray with new values by using Slicing
>>> print(ba,type(ba),id(ba))----bytearray(b'z{\xff8\x00N\xac') <class 'bytearray'> 1857607506160
>>> for val in ba:
...		print(val)
...
			122
			123
			255
			56
			0
			78
			172
===========================================x=============================================

"""


ex3=[10,20,103,40,50,234,70,80,225,100]
ex4=bytearray(ex3)
print(ex4[3],"\n")#print only index wise other wise range or for loop
# for i in ex4:
#     print(i)


for i in ex4[0:7]: #range wise print
   print(i)

print('=============or=====================')

#if i want to ptint in reverse order
for i in range(len(ex4)-1,-1,-1):
    print(ex4[i])

print("=================or=====================") #or

for i in ex4[::-1]:
    print(i)

print("---------------ex2-----------------------\n")

ex4[4]=200
print(ex4,"\n")
for i in ex4:   
    print(i)


print("---------------ex3-----------------------\n")

ex5=[10,20,30,40,50,60,70,80,90,100]
ex6=bytearray(ex5)
print(ex6)









