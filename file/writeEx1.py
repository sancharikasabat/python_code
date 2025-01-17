 #w.p.p which will rite data on the file
"""

             =======================================================
					Writing the Data to the File
			=======================================================
=>To write the Data to the File, we have Two Pre-Defined Functions present in the object of File Pointer . They are
				1. write()
				2. wrilines()
-----------------------------------------------------------------------------------------------------------------------------------------------------
1. write()
-----------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:    FilePointerobj.write(str data)
=>This function is used for writing any type of Data to the File in the form of str.
=>If we have non-str data then we must convert into str and we must write that str to the file.
-----------------------------------------------------------------------------------------------------------------------------------------------------
2. writelines()
-----------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:    FilePointerobj.writelines(str(Iterable-object))
=>This function is used for writing any Iterable Object type  to the File in the form of str.
-----------------------------------------------------------------------------------------------------------------------------------------------------
NOTE: The above Two Functions writes the Data to the file in the form of Value by Value (It is one of the Limitation--we 
            want all the values to write at a time to File)
-------------------------------------------------------------------------------------------------------------------------

"""
name = "Rahul"
sno=10
marks=90.43
with open("std.data", "w") as f:
	f.write(name + "\t")
	f.write(str(sno ) + "\t")
	f.write(str(marks))


print("Data Written to the File")































