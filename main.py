#!/usr/bin/env python

import os

from configuration import DATA_DIR
from lexicon import Lexicon


def alternative_scenario():
    """ Создание лексикона по файлу с примерами. """
    data_filepath = os.path.join(DATA_DIR, 'sample.txt')
    sample_lexicon = Lexicon.load_from_file(data_filepath)
    for _ in range(7):
        print(sample_lexicon.get_phrase())


def main_scenario():
    """ Самый базовый пример генерации персонажа. """
    from character import Location
    from lexicon import SAMPLE_LEXICON
    location = Location(SAMPLE_LEXICON)
    print(location.character)


if __name__ == '__main__':
    alternative_scenario()
