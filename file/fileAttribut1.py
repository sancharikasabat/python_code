# w.p.p which demonstraight file pointer attribute
try:
    a=open("firstMode.data","r")
except  FileNotFoundError:
    print("file not exist")
else:
    print("open file successfully")
    print("file name:" ,a.name )
    print("file mode: " ,a.mode)
    print("file closed or not: " ,a.closed)
    print("if file is readable: " , a.readable())
    print("if file is writable: " , a.writable())
finally:
    print("final block file")
    a.close()
    print("file closed successfully")


    #if i open new file which don't exist then it show some name error . now it handle in ex4.py using with open statement


