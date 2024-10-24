from django import template
import requests, re

register = template.Library()

@register.filter()
def correct_words(value):
    # Используем ТАКОЙ словарь для реалистичности
    req = requests.get('https://raw.github.com/ileygb8cwqogn8c/different_lists/master/Русский%20матерный%20словарь.txt')
    req_add = req.text + ' ' + 'мат' # Добавим одно слово в полученную строку
    for i in req_add.split(): #Создаем список и пробегаем его циклом
        value = re.sub(i.capitalize(), i[0].capitalize() + '*' * (len(i) - 1), value) #Поиск с заглавной буквы
        value = re.sub(i, i[0] + '*' * (len(i) - 1), value, flags=re.IGNORECASE)  #Игнорируем регистр
    return value