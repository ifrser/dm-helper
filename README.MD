**Generate NPC character description**


#### Содержание проекта:
- README.MD -- данное описание репозитория
- character.py -- описание и генерация персонажа
- lexicon.py -- описание структурированных фраз
- main.py -- точка запуска


#### Описание персонажа включает:
- концепция персонажа
(«одноглазый ветеран», «эльфийский лучник», «девочка с потерей памяти»)

Чтобы сгенерировать персонажа, необходимо выбрать/создать лексикон.

```
>>> from character import Location
>>> from lexicon import SAMPLE_LEXICON
>>> location = Location(SAMPLE_LEXICON)
>>> print(location.character)

Character(concept="волченок-оборотень")
```

