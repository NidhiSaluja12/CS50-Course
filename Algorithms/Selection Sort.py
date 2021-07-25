'''Pseudo Code
For i from 0 to n
  find smallest item between ith and last item
  swap smallest item with ith item

'''

def SelectionSort(arr, n):
    if n <= 1:
        return arr
    swaps = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1
    return arr, swaps


arr = list(map(int, input().split()))
n = len(arr)
res = SelectionSort(arr, n)
print(res)
