from dataclasses import dataclass
import random
from typing import List


@dataclass
class Attribute:
    """ Член предложения определение. """
    value: str
    does_go_first: bool = True
    separator: str = ' '

    def describe(self, subject) -> str:
        """ Определение c определяемым.

        :type Subject subject: определяемое
        """
        # TODO: согласованность по числу, роду, падежу, etc
        if self.does_go_first:
            return f'{self.value}{self.separator}{subject.value}'
        else:
            return f'{subject.value}{self.separator}{self.value}'


ATTRIBUTE1 = Attribute('Хромой')
ATTRIBUTE2 = Attribute('Эльфийский')
ATTRIBUTE3 = Attribute('Отважный')
ATTRIBUTE4 = Attribute('Потерянный')
ATTRIBUTE5 = Attribute('с корзинкой', does_go_first=False)
ATTRIBUTE6 = Attribute('который никогда не спит', does_go_first=False, separator=', ')
ATTRIBUTE7 = Attribute('оборотень', does_go_first=False, separator='-')
#
SAMPLE_ATTRIBUTE_LIST = [ATTRIBUTE1, ATTRIBUTE2, ATTRIBUTE3, ATTRIBUTE4, ATTRIBUTE5, ATTRIBUTE6, ATTRIBUTE7]


@dataclass
class Subject:
    """ Член предложение подлежащее. """
    value: str

    def described_by(self, attribute: Attribute) -> str:
        """ Строка описания подлежащего с определением. """
        return attribute.describe(self)


SUBJECT1 = Subject('лесничий')
SUBJECT2 = Subject('волченок')
SUBJECT3 = Subject('банда охотников')
SUBJECT4 = Subject('дерево')
SUBJECT5 = Subject('змеи')
SUBJECT6 = Subject('девочка')
#
SAMPLE_SUBJECT_LIST = [SUBJECT1, SUBJECT2, SUBJECT3, SUBJECT4, SUBJECT5, SUBJECT6]


@dataclass
class SimplifiedPhrase:
    """ Словосочетание из подлежащего и определения. """
    attribute: Attribute
    subject: Subject

    def __str__(self):
        return self.subject.described_by(self.attribute)


SIMPLIFIEDPHRASE1 = SimplifiedPhrase(attribute=ATTRIBUTE1, subject=SUBJECT1)
SIMPLIFIEDPHRASE2 = SimplifiedPhrase(attribute=ATTRIBUTE2, subject=SUBJECT2)
SIMPLIFIEDPHRASE3 = SimplifiedPhrase(attribute=ATTRIBUTE3, subject=SUBJECT3)


@dataclass
class Character:
    """ Персонаж.

    Атрибуты:
     - concept -- образ персонажа, выраженный в самой краткой форме
    """
    concept: SimplifiedPhrase


CHARACTER1 = Character(concept=SIMPLIFIEDPHRASE1)
CHARACTER2 = Character(concept=SIMPLIFIEDPHRASE2)
CHARACTER3 = Character(concept=SIMPLIFIEDPHRASE3)


@dataclass
class Lexicon:
    """ Лексикон местности. """
    attribute_list: List[Attribute]
    subject_list: List[Subject]

    def allow_attribute(self, attribute: Attribute):
        """ Добавить определение в лексикон местности. """
        # TODO: typecheck
        self.attribute_list.append(attribute)

    def allow_subject(self, subject: Subject):
        """ Добавить подлежащее в лексикон местности. """
        # TODO: typecheck
        self.subject_list.append(subject)

    def get_character(self) -> Character:
        """ Сгенерировать персонажа из лексикона данной местности. """
        return Character(
            concept=SimplifiedPhrase(
                attribute=random.choice(self.attribute_list),
                subject=random.choice(self.subject_list)
            )
        )


SAMPLE_LEXICON = Lexicon(attribute_list=SAMPLE_ATTRIBUTE_LIST, subject_list=SAMPLE_SUBJECT_LIST)


if __name__ == '__main__':
    # TODO: unittest
    print(SAMPLE_LEXICON.get_character().concept)
