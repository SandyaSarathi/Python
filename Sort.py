n=int(input())
arr = list(map(int, input().split()))
arr.sort()
l=[print(arr[i],end=" ") for i in range(0,len(arr)-1)]
print(arr[len(arr)-1])
