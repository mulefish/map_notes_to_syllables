
import re

def get_syllables(word):
    # given 'kittycat' return ['kit', 'ty', 'cat]
    word = word.strip()
    word = word.lower()
    regex = '[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy]))?'
    x = re.findall(regex, word)
    return x 


def get_lines_from_file(filename):

    f = open(filename, 'r') 
    lines = f.readlines() 
    
    count = 0
    # Strips the newline character 
    for line in lines: 
        print("Line{}: |{}|".format(count, line.strip())) 
        count += 1 
    return lines

def collect_syllables(words):
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