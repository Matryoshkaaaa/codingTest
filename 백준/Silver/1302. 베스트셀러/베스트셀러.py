N = int(input())

book_list = {}
for _ in range(N):
    words = list(input().split())

    for i in words:
        book_list[i] = book_list.get(i,0)+1

max_word = max(sorted(book_list), key=book_list.get)

print(max_word)