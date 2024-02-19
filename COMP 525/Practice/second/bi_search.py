def find_value(a, v):
    """Binary search to find the index of a value in a sorted list."""
    start_i = 0
    end_i = len(a) - 1
    
    while start_i <= end_i:
        mid = (start_i + end_i) // 2
        if a[mid] == v:
            return mid  # Found the target, return its index
        elif a[mid] < v:
            start_i = mid + 1  # Target is in the right half
        else:
            end_i = mid - 1  # Target is in the left half
    
    return -1  # Target not found in the list

arr = [2, 3, 4, 5, 7, 8, 10, 13]
value_to_find = 7

idx = find_value(arr, value_to_find)

print(f"Value {value_to_find} found at index {idx}.")
