import pandas as pd
import json
import os

# Библиотека для работы с СУБД
from sqlalchemy import engine as sql

# Модуль для работы с отображением вывода Jupyter
from IPython import display

# Создание списков для столбцов таблицы vacancies
IDs = [] # Список идентификаторов вакансий
names = [] # Список наименований вакансий

# Создание списков для столбцов таблицы skills
skills_vac = [] # Список идентификаторов вакансий
skills_name = [] # Список названий навыков


cnt_docs = len(os.listdir('/parser_hh/vacancies'))
i = 0
# Проходимся по всем файлам в папке vacancies
for fl in os.listdir('/parser_hh/vacancies'):
     
    # Открываем, читаем и закрываем файл
    f = open('/parser_hh/vacancies/{}'.format(fl), encoding='utf8')
    jsonText = f.read()
    f.close()
 
    # Текст файла переводим в справочник
    jsonObj = json.loads(jsonText)
 
    # Заполняем списки для таблиц
    IDs.append(jsonObj['id'])
    names.append(jsonObj['name'])

 
    # Т.к. навыки хранятся в виде массива, то проходимся по нему циклом
    for skl in jsonObj['key_skills']:
        skills_vac.append(jsonObj['id'])
        skills_name.append(skl['name'])
 
    # Вывод прогресса выполнения
    i += 1
    display.clear_output(wait=True)
    display.display('Готово {} из {},{} '.format(i, cnt_docs, jsonObj['id']))


# # Создание соединение с БД
eng = sql.create_engine('mysql+pymysql://your_name:pass@name_your_host:port=int/your_db_name')
conn = eng.connect()

# # Создание датафрейма, который сохраняется в БД в таблицу vacancies
df = pd.DataFrame({'id': IDs, 'name': names})
df.to_sql('vacancies', con=conn, schema=None, if_exists='append', index=False)
print('OK') 

# # Тоже самое, но для таблицы skills
df = pd.DataFrame({'vacancy_id': skills_vac, 'skill': skills_name})
df.to_sql('skills', con=conn, schema=None, if_exists='append', index=False)
print('OK') 

# # Закрываем соединение с БД
conn.close()

# Вывод сообщеня об окончании программы
display.clear_output(wait=True)
display.display('Вакансии загружены в БД')
