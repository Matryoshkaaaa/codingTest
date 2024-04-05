def solution(my_string):
    answer = []
    for i in my_string :
        if answer.count(i) == 0 :
            answer.append(i)
    return ''.join(answer)