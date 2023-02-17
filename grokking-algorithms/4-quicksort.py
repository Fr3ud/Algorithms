def quicksort(array):
      if len(array) < 2:
            return array
      
      pivot = array[0]
      less = [i for i in array[1:] if i <= pivot]
      greater = [i for i in array[1:] if i > pivot]

      return quicksort(less) + [pivot] + quicksort(greater)
      

print(quicksort([10, 5, 42, 2, 3, 77]))
