def solution(x):
    print(list(map(int,str(x))))
    a = sum(list(map(int,str(x))))
    print(a)
    if x % a == 0:
        answer = True
    else:
        answer = False
    return answer