def solution(s):
#     print(s.count('p') + s.count('P'))
#     print(s.count('y') + s.count('Y'))
#     if s.count('p') + s.count('P') == s.count('y') + s.count('Y'):
#         return True
#     else:
#         return False

    return s.lower().count('p') == s.lower().count('y')
    
    
