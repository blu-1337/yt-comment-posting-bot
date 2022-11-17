# find th first repeating number

def repeatingArray(arr):
    found = False
    dict = {}
    for i in range(0, len(arr)):
        if arr[i] in dict.values():
            return arr[i];
        else:
            dict[i] = arr[i]
    return False



print(repeatingArray([2,5,1,2,3,5,1,2,4]))
print(repeatingArray([2,1,1,2,3,5,1,2,4]))
print(repeatingArray([2,3,4,5]))


def recur(nr):
    if nr == 1:
        return 1
    if nr == 0:
        return 1
    return nr*recur(nr-1)

def fibo(nr):
    if nr == 0: return 0
    if nr == 1: return 1
    if nr == 2: return 1
    return fibo(nr-2)+fibo(nr-1)

def fibo2(nr):
    if nr == 0: return 0
    if nr == 1: return 1
    if nr == 2: return 1

    a = 1
    b = 1
    new_nr = 0
    while(nr>2):
        new_nr = a + b
        (a,b) = (b, new_nr)
        nr -= 1
    return new_nr



print(recur(5))
print(fibo(7))
print(fibo2(8))
