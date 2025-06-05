n = int(input())

phone_book = {}
for _ in range(n):
    temp = input().lower().split()
    key = temp[1]
    value = temp[0]
    if key in phone_book:
        phone_book[key].append(value)
    else:
        phone_book[key] = [value]
# предварительный вывод: {'женя': ['79184219577', '79281234567'], 'руслан': ['79194249271']}

m = int(input())
for _ in range(m):
    name = input().lower()
    if name in phone_book:
        print(*phone_book[name])
    else:
        print('абонент не найден')
