def find_smallest(array):
    smallest_index = 0
    smallest = array[smallest_index]

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selectionSort(array):
    sortedArray = []

    for i in range(len(array)):
        smallest = find_smallest(array)
        sortedArray.append(array.pop(smallest))
    return sortedArray


print(selectionSort([5, 3, 6, 2, 10]))
