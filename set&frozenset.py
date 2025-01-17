'''
set data type used to store multiple items in a single variable.
set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered and unindexed. 
in set duplicate values are not allowed.
it can be mutable.
it allowed heterogeneous data type.
syntax - set1={10,20,30,40,50}
we can't asses index in set this the main difference between list and set
duplicate values are not allowed in set
we can add a value in set by using add() method
syntax is set.add(value)
we can remove a value in set by using remove() method
syntax is set.remove(value)
set is enclosed in curly braces

'''
ex1={34,87,90,100,500,800,1000,1000}
print(ex1,type(ex1))

ex2={34,87,90,-100,500,500,800,1000,1000}
ex2.add(-10)
print(ex2)
ex2.add(10)
ex2.remove(10)
print(ex2)

print("---------------")

ex3={34,34,87,90,-100,500,800,1000,1000}
ex3.discard(500)# discard() method is used to remove the value from the set
print(ex3)

print("---------------")

ex4={34,87,90,-100,5000,800,1000,1000}
ex4.discard(5000)
print(ex4)

print("---------------")

a=set()
a.add(100)
a.add(200)
a.add(300)
print(a)

print("---------------------frozenset----------------")

ex5=frozenset({34,87,90,-100,5000,800,1000,1000})
print(ex5,type(ex5))    # we can't add or remove any value from frozenset
# ex5.add(100)