def add(a,b):
    return a+b

def counter(func):
    count = 0 
    def inner(*args,**kwargs):
        nonlocal count
        count +=1
        print(f'func {func.__name__} calls {count} times')
        return func(*args,**kwargs)
    return inner
f1 = counter(add)
print(f1(3,5))
print(f1(3,10))
