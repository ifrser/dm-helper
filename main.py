#!/usr/bin/env python
from structure import Character
from structure import Location


def main_scenario():
    """ Самый базовый пример генерации персонажа. """
    forest = Location(
        [
            Character('Хромой лесник'),
            Character('Эльфийский стрелок'),
            Character('Отважный бандит'),
            Character('Потерянный волченок'),
            Character('Девочка с корзинкой'),
        ]
    )
    print(forest.get_character())


if __name__ == '__main__':
    main_scenario()
