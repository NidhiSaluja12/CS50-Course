'''
Pseudo Code:
If only one number 
  Quit
Else
  Divide the array
  Sort left half
  Sort right half
  Merge Sorted halves
  
'''

def Merge_sort(array, size):
    mid = size // 2
    left = array[:mid]
    right = array[mid:]
    
    while len(left) < 1 and len(right) < 1:
        Merge_sort(left)
        Merge_sort(right)

    l_len = len(left)
    r_len = len(right)
    i = j = k = 0
    
    while i < l_len and j < r_len:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


arr = list(map(int, input().split()))
n = len(arr)
Merge_sort(arr, n)
print(arr)

