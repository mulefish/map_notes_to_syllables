
import re
import random

"""
The working metaphore: 
We have many unique syllables and a few wavfiles. Each wavfile will purchase 1 or more syllable. 
Each syllable has its own cost ( determined by how common it is - the more common the more expensive )
"""

def distribute_files_across_syllables(syllables_counts_map, array_of_wavfiles):
    total = 0 
    for k in syllables_counts_map:
        v = syllables_counts_map[k]
        total += v
        print(" {} k {} and v {}".format( total,  k, v ))
    ave = total / len(syllables_counts_map )

    n = len(array_of_wavfiles)


    entries = [] 
    


def find_tripwire(syllables_counts_map, array_of_wavfiles):

    total = 0 
    for k in syllables_counts_map:
        v = syllables_counts_map[k]
        total += v
        print(" {} k {} and v {}".format( total,  k, v ))
    ave = total / len(syllables_counts_map )
    n = len(array_of_wavfiles)

    tripwire = ( ave * n ) / len(array_of_wavfiles)


def shuffle_array_of_objects(array_of_objects):
    random.shuffle(array_of_objects)
    return array_of_objects


def get_syllables(word):
    # given 'kittycat' return ['kit', 'ty', 'cat]

    word = word.strip()
    word = word.lower()
    regex = '[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy]))?'
    x = re.findall(regex, word)
    return x 

def get_lines_from_file(filename):
    # read the file

    f = open(filename, 'r') 
    lines = f.readlines()
    return lines

def collect_syllables(words):
    # take ary of words feed each word into get_syllables and populate a map of syllables and counts
    # return that map 

    seen = {}
    for word in words:
        ary_of_syllables = get_syllables(word)
        for syllable in ary_of_syllables:
            if syllable in seen:
                seen[syllable] += 1
            else:
                seen[syllable] = 1
    return seen


if __name__ == "__main__":
    filename = '10000.txt'
    words = get_lines_from_file(filename)
    collect_syllables(words)