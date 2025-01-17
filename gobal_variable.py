a=10
b=30
def add ():
    a=60
    b=20
    c=a+b
    return c

print(add()) # this return 80 boz when we call fun go and start with line 3 when our func is start

#when we want to add using gobal then should follow syantax

def gbladd():
    a=50
    b=40
    w=globals()['a']
    x=globals().get('b')

    c=a+b+w+x
    return c

print(gbladd())


