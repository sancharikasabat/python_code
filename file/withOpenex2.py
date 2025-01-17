
try:
    with open("firstMode1.data","w") as a:
       print("-------------------------------------")
       print("open file successfully")
       print("file name:" ,a.name )
       print("file mode: " ,a.mode)
       print("file closed or not: " , a.closed)
       print("if file is readable: " , a.readable())
       print("if file is writable: " , a.writable())
       print("-------------------------------------")
    print("print close file:",a.closed )
except  FileNotFoundError:
    print("file not exist")