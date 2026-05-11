def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        min_index = i

        # Find minimum element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# -------- User Input --------

# Take number of elements
n = int(input("Enter number of elements: "))

arr = []

# Take array elements from user
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Print original array
print("\nOriginal Array:", arr)

# Sort array
selection_sort(arr)

# Print sorted array
print("Sorted Array:", arr)