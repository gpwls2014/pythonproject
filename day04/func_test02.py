def add(*args):
    total = 0
    for i in args:
        total += i
    return total

total = add(1,2,3,4,5,6,7,8,9)
print(total)


def add(*args):
    total = 0
    for i in args:
        total += i
    print(total)

add(1,2,3,4,5,6,7,8,9)


