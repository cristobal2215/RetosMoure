def Ordenar(numbers, asc):
    meth_sort = []

    for i in numbers:
        added = False

        for j in range(len(meth_sort)):
            if asc:
                condition = i < meth_sort[j]
            else:
                condition = i > meth_sort[j]
            
            if condition:
                meth_sort.insert(j, i)
                added = True
                break

        if not added:
            meth_sort.append(i)
    
    return meth_sort

print(Ordenar([7, 4, 6, 1, 3, 8, 5, 2], True))
print(Ordenar([7, 4, 6, 1, 3, 8, 5, 2], False))