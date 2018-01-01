def push_front(arr, val):
    arr.append(val)
    for index in reversed(range(len(arr)-1)):
        arr[index], arr[index+1] = arr[index+1], arr[index]
    return arr

arr = [10, 11, 12, 13, 14]
arr =  push_front(arr, 15)
print arr 