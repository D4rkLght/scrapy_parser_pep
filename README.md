![qrkot_spreadsheets_workflow](https://github.com/D4rkLght/scrapy_parser_pep/actions/workflows/scrapy_parser_pep.yml/badge.svg)
# scrapy_parser_pep

### Стек технологий
[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)

## Описание 
Асинхронный парсер для сбора статусов pep с сайта https://peps.python.org/ .
Создаёт два файла с результатом прасинга. В первом файле хранятся номера и статусы pep, а во втором количество статусов.

## Установка
Клонируйте репозиторий:
```
git clone git@github.com:D4rkLght/scrapy_parser_pep.git
```
Создать виртуальное окружение:
```
python -m venv venv
```
Установить зависимости:
```
pip install -r requirements.txt
```

## Запуск парсера
Данные хранятся в файле results.
```
scrapy crawl pep
```

## Над проектом работал:
Разработчик [Ярослав Андреев ](https://github.com/D4rkLght).