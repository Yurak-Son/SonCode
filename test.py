def selection_sort(arr):
    for i in range(len(arr)):
        sel = i
        for j in range(i+1,len(arr)):
            if arr[sel]<arr[j]:
                sel = j
        temp = arr[sel]
        arr[sel] = arr[i]
        arr[i] = temp
    return arr

print(selection_sort([9,8,9,9,9,5])    )
print(selection_sort(['9','8','9','9','9','5']))
