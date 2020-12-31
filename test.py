import unittest
from main import get_syllables, collect_syllables, shuffle_array_of_objects, find_budget, wavs_buy_cheap_syllables, display_to_stout

class TheTests(unittest.TestCase):


    def test_display(self):
        wav_files = ['a', 'b', 'c']
        syllables_cost_map = {
            'a':1,
            'b':1,
            'c':1,
            'd':3,
            'e':4,
            'f':20,
            'g':6,
            'h':7,
            'i':4,
            'j':1,
            'k':1,
            'l':3,
        }
        # set up 
        result = find_budget(syllables_cost_map, wav_files)
        budget = result["budget"]
        results = wavs_buy_cheap_syllables(syllables_cost_map, wav_files, budget)
        files_and_syllables = results["files_and_syllables"]
        map = display_to_stout( files_and_syllables)
        isOk = len(map) == 12 
        self.assertEqual(True, isOk)

    def test_wavs_buy_syllables(self):
        wav_files = ['a', 'b', 'c']
        syllables_cost_map = {
            'a':1,
            'b':1,
            'c':1,
            'd':3,
            'e':4,
            'f':20,
            'g':6,
            'h':7,
            'i':4,
            'j':1,
            'k':1,
            'l':3,
        }

        # get the budet
        result = find_budget(syllables_cost_map, wav_files)
        budget = result["budget"]

        # now test the thing
        results = wavs_buy_cheap_syllables(syllables_cost_map, wav_files, budget)
        count_of_wavs_which_bought_nothing = results["count_of_wavs_which_bought_nothing"]
        count_unpurchased_syllables = len(results["unpurchased_syllables"])

        isOk = count_of_wavs_which_bought_nothing == 0 and count_unpurchased_syllables == 0
        self.assertEqual(True, isOk)

    def test_find_budget(self):

        # Given 3 wav files and 9 syllables where the ave cost of a syllable is 5 find a budget of 15 ( to be given to each wav file later on )

        wav_files = ['a', 'b', 'c']
        syllables_cost_map = {
            'a':1,
            'b':1,
            'c':1,
            'd':3,
            'e':4,
            'f':20,
            'g':6,
            'h':7,
            'i':4
        }
        expected = 15
        # The real answer would be 15.2333 or something like that. Don't care. int 15 is good.
        # I do not really care about the float, but I am vaguely curious _why_ I am getting an int back. 

        # actual = find_budget(syllables_cost_map, wav_files)
        result = find_budget(syllables_cost_map, wav_files)
        actual = result["budget"]
        isOk = expected is actual
        self.assertEqual(True, isOk)

    def test_shuffle_array_of_objects(self):
        given = [
            {'syllable':'a'}, 
            {'syllable':'b'}, 
            {'syllable':'c'}, 
            {'syllable':'d'}, 
            {'syllable':'e'}, 
            {'syllable':'f'}, 
            {'syllable':'g'}, 
            {'syllable':'h'}, 
            {'syllable':'i'}, 
            {'syllable':'j'}, 
            {'syllable':'k'}, 
            {'syllable':'l'}, 
        ]
        # If not shuffled then the 'syllable' keys will yield 'abcdefghijkl'. Do not want that. 
        not_expected = 'abcdefghijkl'
        array_of_objs = shuffle_array_of_objects(given)
        actual = ''
        for obj in array_of_objs:
            actual += obj['syllable']
        isOk = not_expected != actual
        self.assertEqual(True, isOk)


    def test_sort_(self):
        # map = syllable and its count in the corpus
        # Note: The map is much larger than the array of possible wav files 
        syllable_count_map = {
            'pretty_common1': 2,
            'pretty_common2': 2,
            'super_common': 10,
            'unque1':1,
            'unque2':1,
            'unque3':1,
            'unque4':1,
            'unque5':1,
            'unque6':1,
            'unque7':1,
            'unque8':1,
            'unque9':1,
            'unque10':1,
            'unque11':1,
            'unque12':1,
            'unque13':1,
            'unque14':1,
            'unque15':1,
            'unque16':1,
            'unque17':1,
            'unque18':1,
            'unque19':1,

        }
        possible_wav_files = [
            'one.wav',
            'two.wav',
            'three.wav',
            'four.wav',
            'one.wav',
            'one.wav',
            'one.wav',
            'one.wav',
            'one.wav',
            'one.wav',
            'one.wav',
            'one.wav',

        ]


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

        # print("expected len {} ".format( len( expected )))
        # print("actual len {} ".format( len( actual )))
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

    def test_get_3_syllables_with_mixCase_and_paddingSpaces(self):
        given = '  kittyCAt       '
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