from dataclasses import dataclass

from pymorphy2 import MorphAnalyzer
import random
import re
from typing import List

morph = MorphAnalyzer()
sentinel = object()


@dataclass
class Attribute:
    """ Член предложения определение. """
    value: str
    does_go_first: bool = True
    separator: str = ' '

    def describe(self, subject) -> str:
        """ Определение c определяемым.

        :param Subject subject: определяемое

        TODO: type refactor for semantics/syntax/morphology
        """
        word_morph = morph.parse(self.value)[0]
        word_inflection = word_morph.inflect(
            set(
                filter(
                    None,
                    {subject.case, subject.gender, subject.number}
                    )
            )
        )
        inflected_value = (
            word_inflection.word
            if word_inflection is not None
            else self.value
        )
        if self.does_go_first:
            return f'{inflected_value}{self.separator}{subject.value}'
        else:
            return f'{subject.value}{self.separator}{inflected_value}'


ATTRIBUTE1 = Attribute('хромой')
ATTRIBUTE2 = Attribute('эльфийский')
ATTRIBUTE3 = Attribute('отважный')
ATTRIBUTE4 = Attribute('потеряный')
ATTRIBUTE5 = Attribute('с корзинкой', does_go_first=False)
ATTRIBUTE6 = Attribute('который никогда не спит', does_go_first=False, separator=', ')
ATTRIBUTE7 = Attribute('оборотень', does_go_first=False, separator='-')
#
SAMPLE_ATTRIBUTE_LIST = [ATTRIBUTE1, ATTRIBUTE2, ATTRIBUTE3, ATTRIBUTE4, ATTRIBUTE5, ATTRIBUTE6, ATTRIBUTE7]


@dataclass
class Subject:
    """ Член предложения подлежащее. """
    value: str

    def __post_init__(self):
        word_parse = morph.parse(self.value)
        chosen_word_morph = word_parse[0]
        for word_morph in word_parse[1:]:
            if word_morph.tag.case == 'nomn':
                chosen_word_morph = word_morph
                break
            if word_morph.score <= 0.1:
                break
        self.case = chosen_word_morph.tag.case
        self.number = chosen_word_morph.tag.number
        self.gender = (
            chosen_word_morph.tag.gender
            if self.number != 'plur'
            else 'plur'  # TODO: make more strict and general
        )

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

    @property
    def random_subject(self):
        return random.choice(self.subject_list)

    @property
    def random_attribute(self):
        return random.choice(self.attribute_list)

    def get_phrase(self) -> SimplifiedPhrase:
        """ Сгенерировать фразу из местного лексикона.

        TODO: input list of arguments to set phrase parts
        """
        attribute = self.random_attribute
        subject = self.random_subject
        return SimplifiedPhrase(
            attribute=attribute,
            subject=subject
        )

    @staticmethod
    def load_from_file(data_filepath):
        """ Создать лексикон по данным из текстового файла.

        Каждая строка файла представляет словосочетание.
        Главная часть словосочетания выделена квадратными скобками,
        остальная часть зависимая. Если квадратные скобки отсутствуют,
        строка считается главной частью, без зависимой.
        """
        loaded_lexicon = Lexicon([], [])
        with open(data_filepath) as f:
            rows = f.readlines()
        subject_pattern = re.compile(r'\[(.*)\]')
        ending_punctuation_pattern = re.compile(r'[,. -]+$')
        leading_punctuation_pattern = re.compile(r'^[,. -]+')
        for row in (row.rstrip('\n') for row in rows):
            #
            subject_found = subject_pattern.search(row)
            if not subject_found:
                loaded_lexicon.allow_subject(Subject(value=row))
                continue
            #
            subject_value = subject_found.group(1) if subject_found else row
            subject = Subject(value=subject_value)
            #
            attribute_does_go_first = not subject_pattern.match(row)
            attribute_value = subject_pattern.sub('', row)
            punctuation_pattern = ending_punctuation_pattern if attribute_does_go_first else leading_punctuation_pattern
            separator_found = punctuation_pattern.search(attribute_value)
            attribute_separator = separator_found.group(0) if separator_found else ' '
            attribute_value = attribute_value.strip(attribute_separator)
            attribute = Attribute(value=attribute_value,
                                  does_go_first=attribute_does_go_first,
                                  separator=attribute_separator)
            #
            loaded_lexicon.allow_attribute(attribute)
            loaded_lexicon.allow_subject(subject)
            #
        return loaded_lexicon


SAMPLE_LEXICON = Lexicon(attribute_list=SAMPLE_ATTRIBUTE_LIST, subject_list=SAMPLE_SUBJECT_LIST)


if __name__ == '__main__':
    # TODO: unittest
    # TODO: make samples for a class with static method
    for _ in range(7):
        print(SAMPLE_LEXICON.get_phrase())
