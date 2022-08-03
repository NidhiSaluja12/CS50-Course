'''
Pseudo Code:

For i from 0 to size
  If number is at ith position
    return True
    
  Else
    return False

'''




def LinearSearch(arr, n, s):
    result = False
    for i in range(n):
        if arr[i] == s:
            result = True
    return result


arr = list(map(int, input().split()))
n = len(arr)
s = int(input())
res = LinearSearch(arr, n, s)
print(res)

