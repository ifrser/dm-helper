#!/usr/bin/env python


def main_scenario():
    """ Самый базовый пример генерации персонажа. """
    from structure import SAMPLE_LEXICON
    print(SAMPLE_LEXICON.get_character().concept)


if __name__ == '__main__':
    main_scenario()
