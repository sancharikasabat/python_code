"""
				=============================================
=>The purpose of Sequnece Category Data Types is that "To Store Seqence of Values in single Object".
=>We have 4 Data Types in Sequnece Category. They are

				1. str
				2. bytes
				3. bytearray
				4. range
"""

ex1="Hello World"
print(ex1,type(ex1),"----------\n")

ex2="sanch"
print(ex2 ,type(ex2),"-----------\n")

ex3="12345"
print(ex3,type(ex3),"-------------\n")

ex4="12efsf&*$"
print(ex4,type(ex4) ,"----------------\n")

#multiline String
ex5="Hello World\nHello World\nHello World"
print(ex5 ,type(ex5),"\n")

ex6=""" hello world 
my name is sanch
i'm pursuing btech in computer science
my home town is berhampur"""
print(ex6)

print("==========================================\n")

ex7=''' hello world 
my name is sanch
i'm pursuing btech in computer science
my home town is berhampur'''
print(ex7)



print("\n=====================operation str index and sliceing=====================\n")
ex8="Hello World"
print(ex8[4] ,"--------")
print(ex8[5],"-------- ")
print(ex8[-4],"-------- ")
print(len(ex8),"--------")



# ex9=3+1j
# print(len(ex9)) #TypeError: object of type 'complex' has no len()

print("\n=====================operation str sliceing=====================\n")

ex9="sancharika"
print(ex9[0:9],"=sancharik")
print(ex9[0:9:2],"=snhrk")
print(ex9[::-1],"=akrihcnas")
print(ex9[0::2],"=snhrk")
print(ex9[:3],"=san")
print(ex9[3:],"=harika")
print(ex9[::],"=sancharika")


