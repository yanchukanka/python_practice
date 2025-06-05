# лаконичный вариант решения задачи про словарь сленга - не мой
mydict = {}

for _ in range(int(input())):
    key, value = input().split(': ')
    mydict[key.lower()] = value

for _ in range(int(input())):
    print(mydict.get(input().lower(), 'Не найдено'))