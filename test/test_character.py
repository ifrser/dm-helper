from unittest import TestCase

from character import Character


class TestCharacter(TestCase):
    """ Unittect character.Character. """

    def test_init(self):
        character = Character(concept='Приятный собеседник')
        #
        assert character.concept == 'Приятный собеседник'



class TestLocation(TestCase):
    pass
