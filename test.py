import unittest
from read import get_syllables

class TheTests(unittest.TestCase):

    def test_get_syllables(self):
        given = 'kittycat'
        expected = ['kit', 'ty', 'cat']
        actual = get_syllables(given)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()