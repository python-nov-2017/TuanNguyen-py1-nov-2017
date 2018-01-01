def selection_sort(arr):
    print "rangeee! ", range(len(arr)-1)
    
    for i in range(len(arr)-1):
        smallest = arr[i]
        for item in arr[i:]:
            if item < smallest:
                smallest = item
        index_of_smallest = arr.index(smallest)
        arr[i], arr[index_of_smallest] = arr[index_of_smallest],arr[i]

    return arr


arr = [6, 5, 3, 1, 8, 7, 2, 4]
print selection_sort(arr)