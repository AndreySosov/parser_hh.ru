# Библиотека работы с HTTP-запросами
import requests 

# Пакет для работы с JSDN-файлами
import json

# Модуль для работы со значением времени
import time

# Модуль для работы с операционной системой
import os

def getPages(page = 0):
    '''Функция запроса страницы.
       page - Индекс страницы
       (по умолчанию начинается с первой страницы)'''

       # Справочник для переменной GET-запроса
       # Значения для указания значений в справочнике 
       # указаны в документации к API hh.ru по ссылке: 
       # https://github.com/hhru/api
    params = {
                'text': 'data engineer',
                'area': 1,
                'page': page,
                'per_page': 100}

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data

        

# Считаем первые Х вакансий
for page in range(0,20):
    jsObj = json.loads(getPages(page))

    # Сохраняем файлы в папку {путь до текущего документа со скриптом}\установить\ваш\путь
    # Определяем количество файлов в папке для сохранения документа с ответом запроса
    # Полученное значение используем для формирования имени документа
    nextFileName = '/parser_hh/pars_vacancies/{}.json'.format(len(os.listdir('/parser_hh/pars_vacancies')))

    # Создаем новый документ, записываем в него ответ запроса, после закрываем
    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(jsObj, ensure_ascii=False, indent=3))

    # Проверка на последнюю страницу, если вакансий меньше 2000
    if (jsObj['pages'] - page) <= 1:
        break

    time.sleep(0.25)

print('Страницы поиска собраны!')
