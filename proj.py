

def mergeSort(L, ascending = True):
    result = []
    if len(L) == 1:
        return L
    mid = len(L) // 2

    arr1 = mergeSort(L[:mid])

    arr2 = mergeSort(L[mid:])

    x, y = 0, 0
    while x < len(arr1) and y < len(arr2):
        if arr1[x] > arr2[y]: # < for descending
            result.append(arr2[y])
            y = y + 1

        else:
            result.append(arr1[x])
            x = x + 1


    result = result +arr1[x:]

    result = result + arr2[y:]
    if ascending == True :
        return result
    else:
        result.reverse()
        return result

list=[3,2,4,1,5,9,7,6]
print(list)
print(mergeSort(list, False))
