T = int(input())

for ts in range(1,T+1):
    a,b = input().split()
    a = int(a)
    b = list(b)
    # print(list(b).pop(a-1))
    b.pop(a-1)
    answer = "".join(b)
    print(answer)

