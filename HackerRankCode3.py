#find the second largest number

n = int(input())
arr = list(map(int, input().split()))
maxnum=max(arr)
while maxnum==max(arr):
    arr.remove(maxnum)
print(max(arr))
