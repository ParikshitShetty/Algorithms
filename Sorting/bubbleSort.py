def bubbleSort(arr:list):
    size = len(arr)
    
    for i in range(size):
        swapped = False
        
        for j in range(0, size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
        
arr = [64, 34, 25, 12, 22, 11, 90, -1]

bubbleSort(arr)
print("Sorted array:",arr)