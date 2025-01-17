'''loop is used when we want to execute a block of code multiple times
loop is two types:
thise are for loop and while loop
*for loop is used when we know the number of times we want to execute the block of code
syntax of for loop is:

1> for variable in range(start,end):
    block of code

*while loop is used when we want to execute the block of code until a condition is true

2> while condition:
    block of code
'''

# write a python program to print the numbers from 1 to 10 using for loop
print("for loop")
for i in range(1,11):
    print(i)

#wite a python program to print the numbers from 1 to 10 using while loop
print("while loop")
i=1
while i<=10:
    print(i)
    i+=1

# write a python program to print the numbers from 1 to 10 using while loop and break statement
print("break statement")
i=1
while i<=10:
    print(i)
    if i==5:
        break
    i+=1

# write a python program to print the numbers from 1 to 10 using while loop and continue statement
print("continue statement")
i=1
while i<=10:
    if i==5:
        i+=1
        continue
    print(i)
    i+=1

#write a python program to take input from the user and print the sum of all the numbers entered by the user until the user enters 0
print("---sum of numbers---")
 
sum=0
while True:
    num=int(input("enter a number: "))
    if num==0:
        break
    sum+=num













