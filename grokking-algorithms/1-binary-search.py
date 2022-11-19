def binary_search(list, needle):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == needle:
            return mid
        if guess > needle:
            high = mid - 1
        if guess < needle:
            low = mid + 1

    return None


list = [1, 3, 5, 7, 9]

print(binary_search(list, 5))
print(binary_search(list, -1))
