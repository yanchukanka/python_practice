# код проверки имени (например, для namedtuple)

import keyword

def check_fieldnames(lst):
    return [word for word in lst if word not in keyword.kwlist and not word.startswith('_')]

check_list = ['Class', 'age', 'class', 'def', '_def', '_age']
correct_fieldnames = check_fieldnames(check_list)
print(f'Допустимые названия полей именованного кортежа: {", ".join(correct_fieldnames)}')