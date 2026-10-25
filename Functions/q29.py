def binary_search(a, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if a[mid] == x:
        return mid
    if x < a[mid]:
        return binary_search(a, x, low, mid - 1)
    return binary_search(a, x, mid + 1, high)

a = [10, 20, 30, 40, 50]
print(binary_search(a, 30, 0, len(a) - 1))