# Goal: map .wav files to common English syllables   
step 0: Have a list of wav files ( about 100ish )  
step 1: Find common syllables in English ( will be about 1000ish)  
step 2: Distribute the wav file 'evenly' across the set of syllable. But! The more popular a given syllable is in actual usage remove the potential of a wav file to be assigned to another syllable ( TODO: Clarity )

# Output 
From the input in 10000.txt this is the sort of map that will be generated:  
'marsh':{'count': 1, 'file': 'a65.mp3'},  
'kie':{'count': 2, 'file': 'a89.mp3'},  
'bye':{'count': 1, 'file': 'guitar8.wav'},  
'gles':{'count': 1, 'file': 'b76.mp3'},  
'ly':{'count': 155, 'file': 'b72.mp3'},  
'dad':{'count': 3, 'file': 'a52.mp3'},  
'flex':{'count': 1, 'file': 'a57.mp3'},  
'cuss':{'count': 1, 'file': 'a76.mp3'},  
'crash':{'count': 1, 'file': 'b81.mp3'},  
'fourth':{'count': 1, 'file': 'b56.mp3'},  
  
Sidenote: That 10000 words generates 4185 unique syllabols.  

# Trivia  
    {  
        'most_seen_count': 425, 'most_seen_syllable': 're',   
        'number_of_syllables_per_wav': 55,  
        'budget': 275, 'ave_cost': 5  
    }  