import unittest
from read import get_syllables

class TheTests(unittest.TestCase):

    def test_get_syllables(self):
        given = 'kittycat'
        expected = ['kit', 'ty', 'cat']
        actual = get_syllables(given)
        self.assertEqual(actual, expected)

    def test_get_3_syllables_mixCase(self):
        given = 'kittyCAt'
        expected = 3
        actual = len(get_syllables(given)) 
        self.assertEqual(actual, expected)

    def test_get_2_syllables(self):
        given = 'kitty'
        expected = 2
        actual = len(get_syllables(given)) 
        self.assertEqual(actual, expected)

    def test_get_1_syllables(self):
        given = 'kit'
        expected = 1
        actual = len(get_syllables(given)) 
        self.assertEqual(actual, expected)

    def test_get_0_syllables_fromImpossible(self):
        given = 'zhgzhz'
        expected = 0
        actual = len(get_syllables(given)) 
        self.assertEqual(actual, expected)

    def test_get_0_syllables_fromNothing(self):
        given = ''
        expected = 0
        actual = len(get_syllables(given)) 
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()