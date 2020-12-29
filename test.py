import unittest
from read import get_syllables, collect_syllables

class TheTests(unittest.TestCase):

    def test_get_collection_from_list_of_words(self):
        given = [
            'dinosaur',
            'dynomite',
            'mightymite',
            'dog',
            'dogs',
            'doggerbank',
            'dogface',
            'kdlflkfakdakdk',
            ''
        ]
        actual = collect_syllables(given)

        expected = {
            'ger':1, 
            'no': 2, 
            'di':  1,
            'mi':  2,
            'dog':  3,
            'mig':  1, 
            'fa':  1,
            'ce':  1,   
            'bank':  1,
            'dy':  1,
            'te':  2,
            'dogs':  1, 
            'hty':  1 
        }

        print("expected len {} ".format( len( expected )))
        print("actual len {} ".format( len( actual )))
        isOk = True 
        for k in expected:
            actual_count = actual[k]
            expected_count = expected[k]
            if actual_count is not expected_count:
                isOk = False
        self.assertEqual(True, isOk)


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