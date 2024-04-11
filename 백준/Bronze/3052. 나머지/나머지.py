dict_num = {}

for _ in range(10):
    num = int(input())
    div_num = num % 42
    dict_num[div_num] = dict_num.get(div_num, 0) + 1

print(len(dict_num))