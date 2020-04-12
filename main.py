#!/usr/bin/env python


def main_scenario():
    """ Самый базовый пример генерации персонажа. """
    from character import Location
    from lexicon import SAMPLE_LEXICON
    location = Location(SAMPLE_LEXICON)
    print(location.character)


if __name__ == '__main__':
    main_scenario()
