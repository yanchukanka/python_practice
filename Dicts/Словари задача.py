s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

s = s.split()  # разобьем список на отдельные слова
mydict = {}  # теперь создадим словарь, где будем хранить ключ(слово) и значение(кол-во повторов)

for i in s:  # через цикл посчитаем повторы с помощью метода count и присвоем каждому ключу свой каунт
    mydict[i] = s.count(i)
# при выводе словарь имеет такой вид: {'orange': 8, 'strawberry': 4, 'barley': 12, ...}

# дальше задача найти MAX значения(!)
max_count = max(mydict.values())

# переходим к финальной части. создаем пустой словарь,куда сохраним результирующие пары ключей и их MAX значений. так как сохранять надо ПАРЫ, пользуемся методом ITEMS()
result = {}
for key, value in mydict.items():
    if value == max_count:  # проверяем, если наше значение равно максимальному
        result[key] = value  # то добавляем пару в результирующий словарь

# если вывести сейчас result, будет {'barley': 12, 'banana': 12}
# но нам надо вывести ТОЛЬКО ОДИН, тот что МЕНЬШЕ в лексикографическом порядке, значит надо вывести banana. пользуемся min

print(min(result))