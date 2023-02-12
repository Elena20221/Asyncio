# Домашнее задание к лекции «Asyncio»
##### В этом задании мы будем выгружать из API персонажей Start Wars и загружать в базу данных.
##### Документация по API находится здесь: SWAPI.
##### Пример запроса: https://swapi.dev/api/people/1/
##### В результате запроса получаем персонажа с ID 1:
~~~
{
    "birth_year": "19 BBY",
    "eye_color": "Blue",
    "films": [
        "https://swapi.dev/api/films/1/",
        ...
    ],
    "gender": "Male",
    "hair_color": "Blond",
    "height": "172",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "mass": "77",
    "name": "Luke Skywalker",
    "skin_color": "Fair",
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-10T13:52:43.172000Z",
    "species": [
        "https://swapi.dev/api/species/1/"
    ],
    "starships": [
        "https://swapi.dev/api/starships/12/",
        ...
    ],
    "url": "https://swapi.dev/api/people/1/",
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/"
        ...
    ]
}
~~~
##### Необходимо выгрузить cледующие поля:  
id - ID персонажа  
birth_year  
eye_color  
films - строка с названиями фильмов через запятую  
gender  
hair_color  
height  
homeworld  
mass  
name
skin_color
species - строка с названиями типов через запятую  
starships - строка с названиями кораблей через запятую  
vehicles - строка с названиями транспорта через запятую  
##### Данные по каждому персонажу необходимо загрузить в любую базу данных.
##### Выгрузка из апи и загрузка в базу должна происходить асинхронно.

##### Результатом работы будет:

* ##### скрипт миграции базы данных
* ##### скрипт загрузки данных из API в базу
##### В базу должны быть загружены все персонажи
