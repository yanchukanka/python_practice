# Задача про валидность пароля
# 1. len(password) >= 8
# 2. содержит ли пароль как минимум одну заглавную букву  isupper()
# 3. содержит ли пароль как минимум одну строчную букву islower()
# 4. содержит ли пароль хотя бы одну цифру isdigit()

def isPasswordGood(password):
    if len(password) < 8:
        return False

    upLetter = False
    lowLetter = False
    num = False

    for i in password:
        if i.isupper():
            upLetter = True
        elif i.islower():
            lowLetter = True
        elif i.isdigit():
            num = True
    return upLetter and lowLetter and num

password = input()

print(isPasswordGood(password))