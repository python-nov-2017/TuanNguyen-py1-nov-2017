def bubble_sort(arr):
    length = len(arr)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr




arr = [6,5,3,1,8,7,2,4]
print arr
print bubble_sort(arr)

