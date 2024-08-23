original = [64, 34, 25, 12, 22, 11, 90, -1]

def bubbleSort() -> dict:
    size = len(original)
    arr = original[:]
    
    for i in range(size):
        swapped = False
        
        for j in range(0, size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return { "original":original, "arr":arr }

if __name__ == "__main__":
    # This will only run if this script is executed directly
    result = bubbleSort()
    print("Bubble Sort Result:", result)