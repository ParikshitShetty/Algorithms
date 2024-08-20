def selectionSort(arr:list, size:int):
    for i in range(size):
        min_index = i
        for j in range( i + 1, size):
            # select the minimum element in every iteration
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)

selectionSort( arr=arr, size=size )

print(arr)