def solution(x, n):
    answer = []
    if x > 0:
        for i in range(x, x * n + 1, x):
            answer.append(i)
    elif x < 0:
        for i in range(x, x * n - 1, x): 
            answer.append(i)
    elif x == 0:  
        return [0] * n  
    return answer
