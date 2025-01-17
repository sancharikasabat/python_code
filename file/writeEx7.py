# reading the data from file and writing it into the file.
try:
  
  srcf=input("Enter the source file name : ")
  with open(srcf,"r") as rf:
    dstf=input("Enter the destination file name : ")
    with open (dstf,"a") as df:
        scrfd=rf.read()
        df.write(scrfd)
        print("source file content writen sucsessfully")
except FileNotFoundError:
   print("file is not exist")
