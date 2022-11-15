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


