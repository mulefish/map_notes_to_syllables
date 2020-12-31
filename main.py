
import re
import random

"""
The working metaphore: 
We have many unique syllables and a few wavfiles. Each wavfile will purchase 1 or more syllable. 
Each syllable has its own cost ( determined by how common it is - the more common the more expensive )
"""

def display_to_stout(files_and_syllables, syllables_cost_map):
    """
    Convert from something like this: 
    [{'syllables': ['e', 'f'], 'budget': -8, 'filename': 'b'}
        {'syllables': ['g', 'h'], 'budget': 3, 'filename': 'c'}
        {'syllables': ['a', 'i', 'l', 'k', 'j', 'b', 'd', 'c'], 'budget': 1, 'filename': 'a'}] 
    
    to something javascript friendly like this: 
    {
    'a':{'count': 1, 'file': 'a'},
    'c':{'count': 1, 'file': 'a'},
    'b':{'count': 1, 'file': 'a'},
    'e':{'count': 4, 'file': 'c'},
    'd':{'count': 3, 'file': 'a'},
    'g':{'count': 6, 'file': 'b'},
    'f':{'count': 20, 'file': 'b'},
    'i':{'count': 4, 'file': 'a'},
    'h':{'count': 7, 'file': 'c'},
    'k':{'count': 1, 'file': 'a'},
    'j':{'count': 1, 'file': 'a'},
    'l':{'count': 3, 'file': 'a'}
    }
    """
    map = {} 
    for obj in files_and_syllables:
        filename = obj["filename"]
        for syllabol in obj["syllables"]:
            map[syllabol] = filename 

    print("\n{")
    i = 0
    for k in map: 
        payload = {"file":map[k], "count":syllables_cost_map[k]}
        if i < len(map) - 1:
            print("'{}':{},".format(k, payload))
        else:
            print("'{}':{}".format(k, payload))
        i += 1 
    print("}")
    return map 

def wavs_buy_syllables(syllables_costs_map, array_of_wavfiles, budget):

    """
    step1: convert from a simply key-value map of 'syllable names' and 'costs' to a
    shuffled array of objects that has 'syllable' and 'cost'.
    ...
    The main purpose of step1 is to have an array to shuffle. If I knew how to shuffle a map I would not bother
    with this step. 
    """ 
    syllables = [] 
    for syllable in syllables_costs_map:
        cost = syllables_costs_map[syllable]
        obj = {
            "syllable":syllable,
            "cost":cost, 
            "purchased": False
        }
        syllables.append(obj)
    syllables = shuffle_array_of_objects(syllables)

    """
    step2: make a map with the items of the array_of_wavfiles providing the keys. 
    On each item in that map give it a object with a 'budget' ( int ) and a array of syllables
    """
    HoH = {}
    for filename in array_of_wavfiles:
        HoH[filename] = {
            "filename":filename,
            "budget":budget,
            "syllables":[]
        }

    """
    step3: roll through each item in the HoH and purchase as many syllables as its budget will allow.
    """
    limit = 1
    loop = 0
    for filename in HoH:
        obj = HoH[filename]
        recurse(obj, syllables, 0)

    """
    step4a: 
    None of the really expensive syllables will have been bought yet. 
    Step 3 was to spread out the cheap ones.
    Now to force the purchesing of the left over expensive ones. 
    """ 
    unpurchased = [] 
    for syllable in syllables: 
        if syllable["purchased"] is False:
            unpurchased.append(syllable)

    # for up in unpurchased:
    #      print(" unpurchased {}".format(up)  )

    """
    step4b:
    Convert that HoH to a LoH and revere sort it so the richest ones are on top.
    Roll through each of the unpurchased syllables and force someone to buy them.
    """
    LoH = [] 
    for k in HoH:
        LoH.append(HoH[k])
    LoH.sort(key=lambda x: x["budget"], reverse=True)

    index = 0 
    for syllable in unpurchased:
        syllable["purchased"] = True 
        LoH[index]["budget"] -= syllable["cost"] # Likely will make the  budget be negative. That is ok. Actually it does not matter, but I might use that information later on. 
        LoH[index]["syllables"].append(syllable["syllable"])

    leftover = []
    for syllable in unpurchased: 
        if syllable["purchased"] is False:
            leftover.append(syllable)

    count_of_wavs_which_bought_nothing = 0
    for obj in LoH:
        if len(obj["syllables"]) == 0:
            count_of_wavs_which_bought_nothing += 1 

    results = {
        "files_and_syllables": LoH, 
        "unpurchased_syllables":leftover, # better have length of 0 
        "count_of_wavs_which_bought_nothing": count_of_wavs_which_bought_nothing # better be 0
    }

    return results

LOOP_LIMIT = 40
def recurse(obj, syllables, loop):
    loop += 1 

    if loop < LOOP_LIMIT: 
        for item in syllables: 
            cost = item["cost"]
            # print( "{} cost {} --> {} ".format( loop, cost, item )) 
            if item["purchased"] is False:
                if obj["budget"] - cost > 0: 
                    obj["budget"] -= cost
                    item["purchased"] = True 
                    obj["syllables"].append(item["syllable"])
        recurse( obj, syllables, loop )


def find_budget(syllables_costs_map, array_of_wavfiles):
    """
    find the ave cost. 
    find len(syllables) / len(wavs ) and multipy that # by the ave cost. 
    this will be the 'max budget' that each wav will be given 

    NOTE: It will be OK to be a little sloppy...  Ints are fine...  I will clean up/deal with any slop later on.

    """ 

    total = 0 
    most_seen_count = 0 # not needed - just I am curious to find the most common English syllable
    most_seen_syllable = '' # not really needed - just I am curious to find the most common English syllable
    for k in syllables_costs_map:
        v = syllables_costs_map[k]
        total += v

        # not really needed - just I am curious to find the most common English syllable
        if most_seen_count < v:
            most_seen_count = v
            most_seen_syllable = k

    ave_cost = total / len(syllables_costs_map )
    number_of_syllables_per_each_wav = len(syllables_costs_map) / len(array_of_wavfiles)
    budget = ave_cost * number_of_syllables_per_each_wav
    # return budget 

    # Actually only need the 'budget' but I am curious about the other things
    result = {
        'budget': budget,
        'ave_cost': ave_cost, 
        'number_of_syllables_per_wav':number_of_syllables_per_each_wav, 
        'most_seen_syllable':most_seen_syllable,
        'most_seen_count':most_seen_count
    }
    return result

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

    wavs_array= [ 'FernhillPark.wav', 'FoodVillaMarket.wav', 'NE33rdAve.wav', 'a48.mp3', 'a49.mp3', 'a50.mp3', 'a51.mp3', 'a52.mp3', 'a53.mp3', 'a54.mp3', 'a55.mp3', 'a56.mp3', 'a57.mp3', 'a65.mp3', 'a66.mp3', 'a67.mp3', 'a68.mp3', 'a69.mp3', 'a70.mp3', 'a71.mp3', 'a72.mp3', 'a73.mp3', 'a74.mp3', 'a75.mp3', 'a76.mp3', 'a77.mp3', 'a78.mp3', 'a79.mp3', 'a80.mp3', 'a81.mp3', 'a82.mp3', 'a83.mp3', 'a84.mp3', 'a85.mp3', 'a86.mp3', 'a87.mp3', 'a88.mp3', 'a89.mp3', 'a90.mp3', 'b49.mp3', 'b50.mp3', 'b52.mp3', 'b53.mp3', 'b54.mp3', 'b56.mp3', 'b57.mp3', 'b66.mp3', 'b67.mp3', 'b68.mp3', 'b69.mp3', 'b71.mp3', 'b72.mp3', 'b73.mp3', 'b74.mp3', 'b76.mp3', 'b79.mp3', 'b80.mp3', 'b81.mp3', 'b83.mp3', 'b84.mp3', 'b86.mp3', 'b87.mp3', 'b89.mp3', 'b90.mp3', 'crow3.wav', 'dog1.wav', 'guitar1.mp3', 'guitar2.wav', 'guitar3.wav', 'guitar4.wav', 'guitar5.wav', 'guitar6.wav', 'guitar7.wav', 'guitar8.wav', 'neeya.wav' ]
    filename = '10000.txt'
    words = get_lines_from_file(filename)
    # 'cost' = number of times each unique syllable was seen in the corpus
    syllables_costs_map = collect_syllables(words)

    
    """
    results_map trivial! Out of the 10000.txt file 're' is most common syllable. 
    ave syllable seen 5 times, 
    but 're' was seen 425 times!
    ...
    Anyhow, only acutally care about the 'budget' value that is on the results_map
    """
    results_map = find_budget(syllables_costs_map, wavs_array) 

    # {'most_seen_count': 425, 'most_seen_syllable': 're', 'number_of_syllables_per_wav': 55, 'budget': 275, 'ave_cost': 5}
    # print(results_map)
    
    budget = results_map['budget']
    results = wavs_buy_syllables(syllables_costs_map, wavs_array, budget)
    files_and_syllables = results["files_and_syllables"]
    display_to_stout(files_and_syllables, syllables_costs_map)
    print("The end")