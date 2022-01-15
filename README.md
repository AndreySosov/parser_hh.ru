# Панриснг вакансий с сайта hh.ru
## Сбор вакансий по ключевому слову и навыков к ним. 

### Алгоритм действий:

1) В скрипте **connection_hh_api.py** устанавливаем необходимые значения в функции **getPages**
в переменной **params** (text - 'ключевое слово поиска'
                         area - цифровое обозначения региона поиска 
                         (нужное значение можно найти в справочнике регионов по ссылке **https://github.com/hhru/api/blob/master/docs/areas.md**)
                         page - номер страницы, с которой нужно начать сбор информации
                         per_page - колличество вакансий наодной странице)

2) Необходимо запустить скрипт

3) Далее, запускаем скрипт **retrieving_vacancies.py**. Который вытаскивает вакансии в отдельные JSON-файлы. Для последующей обработки

4) Загружаем данные, в заранее созданную базу данных SQL, с помощью скрипта **load_to_database.py**. В переменной **eng**, в строке аргумента **sql.create.engine**,
вписываем свою СУБН, с которой работаете. А так же свом пароли, хосты и т.д.) 
**Примечание:** Библиотека для работы с СУБД используется - sqlalchemy. Убедитесь, что ваша СУБД поддерживается 
Информацию по поддержке и по способу подключения разных СУБД можно посмотреть по ссылке **https://docs.sqlalchemy.org/en/14/core/engines.html**

5) После того, как данные собраны в БД, запускаем скрипт **report.ipynb**. В переменной **conn** задаем те же параметры подключения, что и при подключении к БД в пункте 4 в своем Jupyter-блокноте. В переменной **cv**, объекте класса **CountVectorizer** можно установить stop_words, чтобы отсеять нерелевантные значения.

Итог, получаем биграмму профессий:

![](https://user-images.githubusercontent.com/77112597/149620856-1fa69b65-28d3-40dd-be22-03c17e29715e.jpg)

Нажав на любую биграмму, получаем название вакансий и ТОП-20 навыков к ним:

![](https://user-images.githubusercontent.com/77112597/149620947-4d60a92a-9d47-44a7-86cb-4e9e497db107.jpg)
