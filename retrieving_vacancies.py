import json
import os
import requests
import time

# Получаем перечень ранее созданных файлов со списком вакансий и проходимся по нему в цикле
for fl in os.listdir('/parser_hh/pars_vacancies'):
	f = open('/parser_hh/pars_vacancies/{}'.format(fl), encoding='utf8')
	jsonText = f.read()
	f.close()

	jsonObj = json.loads(jsonText)

	for vacancies in jsonObj['items']:
		req = requests.get(vacancies['url'])
		data = req.content.decode()
		req.close()

		fileName = '/parser_hh/vacancies/{}.json'.format(vacancies['id'])
		file = open(fileName, mode='w', encoding='utf8')
		file.write(data)
		file.close()

print('Вакансии собраны')
