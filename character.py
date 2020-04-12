from dataclasses import dataclass

from lexicon import Lexicon
from lexicon import SAMPLE_LEXICON
from lexicon import SimplifiedPhrase
from lexicon import SIMPLIFIEDPHRASE1
from lexicon import SIMPLIFIEDPHRASE2
from lexicon import SIMPLIFIEDPHRASE3


@dataclass
class Character:
    """ Персонаж.

    Атрибуты:
     - concept -- образ персонажа, выраженный в самой краткой форме
    """
    concept: SimplifiedPhrase

    def __str__(self):
        return f'{self.__class__.__name__}(concept="{self.concept}")'


CHARACTER1 = Character(concept=SIMPLIFIEDPHRASE1)
CHARACTER2 = Character(concept=SIMPLIFIEDPHRASE2)
CHARACTER3 = Character(concept=SIMPLIFIEDPHRASE3)


@dataclass
class Location:
    """ Место обитания персонажей. """
    lexicon: Lexicon

    @property
    def character(self) -> Character:
        """ Персонаж, встречающийся в данной местности. """
        return Character(
            concept=self.lexicon.get_phrase()
        )


LOCATION1 = Location(SAMPLE_LEXICON)


if __name__ == '__main__':
    # TODO: unittest
    # TODO: make samples for a class with static method
    print(LOCATION1.character)