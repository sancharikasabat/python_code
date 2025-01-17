#syntax=filter function name ,itrable object

#filter the postive number of list using lambda fun

def pos (val):
   
     if val>0:
       return True
     else :
        return False


# pos=lambda x: x>0

     

lst=[23,45,43,-23,56,76,87,-90,-76,-97]
fil=list(filter(pos,lst)) #convestion is imp list
print(fil)

