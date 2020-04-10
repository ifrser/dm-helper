from dataclasses import dataclass
from dataclasses import field
import random
from typing import List


@dataclass
class Character:
    """ Персонаж. """
    concept: str


@dataclass
class Location:
    """ Место обитания персонажей. """
    character_list: List[Character] = field(default_factory=list)

    def allow_character(self, character):
        """ Разрешить персонажу находиться в локации. """
        self.character_list.append(character)

    def get_character(self):
        """ Сгенерировать персонажа для данной локации. """
        return random.choice(self.character_list)


if __name__ == '__main__':
    x = Character('Эльфийский лучник')
    print(x)
    y = Location()
    y.allow_character(x)
    print(y)
