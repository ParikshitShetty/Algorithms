original = [12, 11, 13, 5, 6]

def insertionSort() -> dict:
    arr = original[:]
    
    for i in range(1, len(arr)):
        pointer = arr[i]
        j = i - 1
        
        while j >= 0 and pointer < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pointer
    
    return { "original":original, "arr":arr }

if __name__ == '__main__':
    result = insertionSort()
    print(f"Sorted using Insertion Sort: {result}")