def Ordenar(numbers, asc):
    meth_sort = []

    for number in numbers:
        added = False

        for i in range(len(meth_sort)):
            if asc:
                condition = number < meth_sort[i]
            else:
                condition = number > meth_sort[i]
            
            if condition:
                meth_sort.insert(i, number)
                added = True
                break

        if not added:
            meth_sort.append(number)
    
    return meth_sort

print(Ordenar([7, 4, 6, 1, 3, 8, 5, 2], True))
print(Ordenar([7, 4, 6, 1, 3, 8, 5, 2], False))