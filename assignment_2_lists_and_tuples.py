arr=[(2,5),(1,2),(4,4),(2,3),(2,1)]
n=len(arr)
for i in range(n-1):
    for j in range(0, n-i-1):
        if arr[j][1] > arr[j + 1][1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
