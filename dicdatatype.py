'''dic is the data type in python which is used to store the data in key value pair
syntax of dic is {key:value}
key is unique and value can be duplicate
key can be of any data type but value can be of any data type
key can be any immutable data type like int,float,string,tuple
value can be any data type like int,float,string,list,tuple,dict
'''
#empty dic
d={}
print(type(d))
print(d)

#dic with some data
d1={1:'one',2:'two',3:'three'}
print(d1)
print(type(d1))

#dic with duplicate value
d2={1:'one',2:'two',3:'one'}
print(d2)

#dic with duplicate key
d3={1:'one',2:'two',1:'one'}
print(d3)

print("=======dic with different data type====")
d4={1:'one',2:'two',3:'three',4:4.5,5:(1,2,3)}
print(d4)

print("======dic with list as value============")
d5={1:'one',2:'two',3:'three',4:[1,2,3]}
print(d5)










