def counter(name):
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(f'{name} calls me {count} times')
        # return f'{name} calls me {count} times'
    return inner
c = counter('sasha')
c()
c()
m = counter('max')
m()
c()


def adder(a):
    def inner(b):
        return a+b
    return inner
a2 = adder(2)
print(a2(5))
print(a2(10))
a5 = adder(5)
print(a5(10))
print(a2(100))



def average_numbers():
    summ = 0
    count = 0
    def inner(n):
        nonlocal summ
        nonlocal count
        count +=1
        summ +=n
        return summ/count
    return inner
n = average_numbers()
print(n(5))
print(n(35))