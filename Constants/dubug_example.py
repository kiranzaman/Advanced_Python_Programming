def my_sort(arr):
    if __debug__:
        print("Debug mode is ON!")
    else:
        print("Optimized mode: Debug OFF!")
    return sorted(arr)

print(my_sort([3, 2, 1]))
