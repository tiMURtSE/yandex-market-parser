## TODO

## ADD
    - Ускорить работу парсера
        + Проверять наличие описания от YandexGPT только, если есть отзывы
    - Добавить вывод для описания от YandexGPT
    - Добавить пролистывание на следующую страницу
    - Создать общий класс для Review

## FIX
    - Если есть вариант просмотра отзывов у всех продавцов, то открывать именно такую страницу
        - Можно пропускать следующие товары такого же артикула (?)
    - Задержка через time.sleep() в классе SearchResultPage
    - Убрать запись одинаковых отзывов для одного товара