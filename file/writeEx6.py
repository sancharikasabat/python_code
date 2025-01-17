# reading the data from kb and writing it into the file.

a = input("enter something about hyd data : ")
with open("hyd.data" , "a") as f:
    f.write(a + "\n")
    print ("successfully written into the file")