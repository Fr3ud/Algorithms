def binary_search(array, needle):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high)
        guess = array[mid]

        if guess == needle:
            return mid
        if guess > needle:
            high = mid - 1
        if guess < needle:
            low = mid + 1

    return None


array = [1, 3, 5, 7, 9]

print(binary_search(array, 5))
print(binary_search(array, -1))
