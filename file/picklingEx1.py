import pickle
def saveemdata():
  
           #using for loop 
     while(True):
        try:  
            with open("empdata.pick","ab") as fb:
                #read the em data from kb
                print("---------------------")
                sno=int(input("Enter the employee no:"))
                name=str(input("Enter the name of employe:"))
                salery=int(input("Enter the salery "))
                print("----------------------")
                
                lst=[]
                lst.append(sno)
                lst.append(name)
                lst.append(salery)
                #save the iterble data in the file 
                pickle.dump(lst,fb)
                print("emp rcd saved sucsessfully")
                ch=input(("Do u want anther records (yes/no)"))
                if (ch.lower()== "no"):
                    print("thank you")
                    break
        except ValueError:
         print("read again enter correct input please  ")


 #main  
saveemdata()