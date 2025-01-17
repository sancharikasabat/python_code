a=300
b=67
def sum():
  x=globals()['a']
  y= globals()['b']

  c=x+y
  return c

add=sum()
print(f' the sum {a} and {b} is  :{add}')