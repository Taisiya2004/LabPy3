import re

def check_russian_postal_code(postal_code):
    pattern = r'\b\d{6}\b'  # шаблон для российского почтового индекса (6 цифр)
    return bool(re.match(pattern, postal_code))

# Получение ввода от пользователя
user_input = input("Введите почтовый индекс России: ")

# Проверка введенной строки
if check_russian_postal_code(user_input):
    print("Это корректный почтовый индекс России")
else:
    print("Это не почтовый индекс России или он некорректен")