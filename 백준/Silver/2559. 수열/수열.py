import sys
input = sys.stdin.readline

N, K = map(int,input().split())

nums = list(map(int,input().split()))

max_sum = sum(nums[:K])
current_sum = max_sum

for i in range(1,N-K+1):
    current_sum = current_sum - nums[i-1] + nums[i+K-1]
    max_sum = max(current_sum,max_sum)

print(max_sum)