# demonstraigting the iterable object 

x=["a",23.4,23,"a+3j",45]
f=open("std3.data" , "a")
f .writelines  (str(x)) # with converstion it show error

print("writen itereable obj sucsussfully")

f.close()