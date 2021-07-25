'''
Pseudo Code :

Repeated until sorted
  For i from 0 to n(size)
    If ith and i+1th element out of order
    swap them
  If no swaps
    Quit

'''

def BubbleSort(array, size):
    for i in range(size):
        for j in range(i+1, size):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


arr = list(map(int, input().split()))
n = len(arr)
res = BubbleSort(arr, n)
print(res)
