def search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2 # make sure to round it down
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
n,k = map(int,input().split())
a = list(map(int, input().split()))[:n]
b = list(map(int, input().split()))[:k]
for i in range (len(b)):
    if search(a,b[i]) == -1:
        print("NO")
    else:
        print("YES")