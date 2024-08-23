original = [-2, 45, 0, 11, -9,88,-97,-202,747]

def selectionSort() -> dict:
    size = len(original)
    arr = original[:]
    for i in range(size):
        min_index = i
        for j in range( i + 1, size):
            # select the minimum element in every iteration
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return { "original":original, "arr":arr }

if __name__ == "__main__":
    # This will only run if this script is executed directly
    result = selectionSort()
    print("Selection Sort Result:", result)