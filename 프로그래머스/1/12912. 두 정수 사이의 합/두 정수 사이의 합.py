def solution(a, b):
    answer = 0
    if a < b:
        for x in range(a, b + 1):  
            answer += x
    elif a > b:
        for x in range(b, a + 1):
            answer += x
    elif a == b:
            print(a)
            answer = a
    
    return answer
