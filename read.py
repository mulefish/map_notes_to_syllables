
import re

def get_syllables(word):

    """
    # Trying to make this python be the equivilent of this javascript: 
    const syllableRegex = /[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy]))?/gi;
    function syllabify(word) {
        word = word.trim();
        const syllables = word.match(syllableRegex);
        return syllables;
    }
    """

    # matched = re.search('(/[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy]))?/gi)', word)

    # this returns ('kit') from 'kittycat'

    matched = re.search('([^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy])))?', word)
    if matched:
        tokens = matched.groups()
        print(tokens) 
        print("YAY from {}".format( word ))
    else:
        print("NOPE from {}". format( word ))
    return ['kit', 'ty', 'cat']






def get_lines_from_file(filename):

    f = open(filename, 'r') 
    lines = f.readlines() 
    
    count = 0
    # Strips the newline character 
    for line in lines: 
        print("Line{}: |{}|".format(count, line.strip())) 
        count += 1 
    return lines


## 
if __name__ == "__main__":
    filename = '10000.txt'
    lines = get_lines_from_file(filename)
