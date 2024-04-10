import sys
input = sys.stdin.readline

N, M = map(int,input().split())

nums = list(map(int,input().split()))
arr = [0]
arr_num = 0
for num in nums:
    arr_num += num
    arr.append(arr_num)

for _ in range(M):
    i,j = map(int,input().split())
    answer = arr[j] - arr[i-1]
    print(answer)