


'''
Pseudo Code:

If number is middle
  return True
elif number < middle
  search left half
elif number > middle
  search right half
If no element
  return False


'''

def BinarySearch(arr, n, s):
    arr.sort()
    result = False
    mid = n//2
    left = arr[:mid]
    right = arr[mid:]

    if arr[mid] == s:
        return True

    elif s < arr[mid]:
        for i in range(0, mid):
            if arr[i] == s:
                return True

    elif s > arr[mid]:
        for i in range(mid+1, n):
            if arr[i] == s:
                return True

    return result


arr = list(map(int, input().split()))
n = len(arr)
s = int(input())
res = BinarySearch(arr, n, s)
print(res)
