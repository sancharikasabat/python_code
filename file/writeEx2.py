name=input("enter the name:")
age=int(input("enter the age:"))
mark=float(input("enter the mark:"))
with open ("std.data","a") as f:
    f.write(name + "\n")
    f.write(str(age )+ "\n")
    f.write (str(mark )+ "\n")
   
print("data written successfully")   