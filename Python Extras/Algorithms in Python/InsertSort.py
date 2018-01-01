def insert_sort(arr):
    for i in arr:
        j = arr.index(i)
        while j>0:
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j-1
    return arr

arr = [6, 5, 3, 1, 8, 7, 2, 4]
print arr
print insert_sort(arr)