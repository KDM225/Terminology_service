# Terminology Service


# Описание

Это API является сервисом терминологии, в который входят справочники и его элементы.

### Дополнительные сведения

В проекте есть готовая документация Postman. Она находится в основной директории - `terminology_service.log`

## Установка

Для начала работы нужно:
 - установить все необходимые библиотеки из `requirements.txt`
 - В PostgreSQL создать новую базу данных - `CREATE DATABASE terminology_service`
 - В самом проекте, используя виртуальное окружение (`source venv/bin/activate`),
   применить миграции к пустой базе данных - `python manage.py makemigrations`, `python manage.py migrate`
   
## Запросы

С API можно взаимодействовать при помощи http-запросов.
Далее будут показаны примеры возможных сценариев работы приложения.

### Catalog
***
#### *GET*
Получение списка справочников

Method = `get`

URL:
```text
/api/catalogs_list/
```

Ответ:
```json
{
    "catalogs_list": [
        {
            "name": "Философия"
        },
        {
            "name": "Информатика"
        }
    ]
}
```
***
##### *DELETE*
Удаление справочника по идентификатору

Method = `delete`


URL:
```text
/api/catalogs/:id
```

#### *GET*
Получение списка справочников на указанную дату

Method = `get`

URL:
```text
/api/catalogs_list_date/?start_date=some date
```

Ответ:
```json
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "start_date": "2020-11-27T07:10:13Z",
            "version": "1",
            "element": {
                "code_element": "Абстрагирование",
                "value_element": "процесс мысленного отвлечения"
            }
        }
    ]
}
```

#### *GET*
Получение элементов заданного справочника указанной версии

Method = `get`

URL:
```text
/api/catalog_element_version/?name=some name&version=some version
```

Ответ:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Философия",
            "short_name": "Фил",
            "description": "наука, первоначально исследовавшая количественные отношения и пространственные формы",
            "version": {
                "version": "2",
                "start_date": "2020-11-27T18:45:31Z",
                "element": {
                    "code_element": "Агностицизм",
                    "value_element": "философское учение, отрицающее принципиальную возможность познания человеком объективного мира."
                }
            }
        }
    ]
}
```
***
