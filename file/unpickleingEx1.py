#wtite a python program which will the records  file (emp.pick )file by using unpickleing .
#reading the file 
import pickle
def unpickeledata():
  try:
    with open("empdata.pick","rb") as fb:
       record= pickle.load(fb)
       print(type(record))
  
  except FileNotFoundError:
    print("file not exist")

#main 
unpickeledata()