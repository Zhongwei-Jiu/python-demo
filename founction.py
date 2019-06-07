

def func (x,y):

    if x > y:
        return x
    elif x < y:
        return y
    else:
        return 'x is equal to y'



print(func(2,2))
print(func.__doc__)
