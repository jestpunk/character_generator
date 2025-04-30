### Структура проекта

Генератор случайно генерирует персонажей (среди некоторых огранчиений — кол-во очков, распределяющихся по характеристикам / количество золота)

Имена также генерируются случайно (n-граммы)

Портрет — ASCII-арт, генерируемый из заготовок (глаз, носов, ушей и так далее)

Сущности внутри проекта:
- Персонаж
- Характеристика (одна характеристика может влиять на другую)
- Класс
- Раса
- Имя
- Инвентарь
- Портрет

```
main.py (CLI)

lib
—> core
   —> character.py
   —> portait.py
   —> item.py
—> name
   —> name_generator.py
   -> some_names.txt / csv
—> portrait
   —> drawer.py
   —> components.py
   
   items.py
   characteristics.py
   generator.py

tests
—> test_name.py
—> test_portrait.py
—> test_generator.py
```