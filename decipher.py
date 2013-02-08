# decipher.py
# Ouput your top 3 words on one single line separated by the space
# character to the text file RESULT.OUT

import string

try:
    infile = open("MYSTERY.IN", "r") # open file for reading
    outfile = open("RESULT.OUT", "w")  # open file for writing
    lines = infile.readlines()
    new = ''
    words = []
    
    for line in lines:
        for letter in line:
            new += str(chr(ord(letter)-5))
    
# find position of spaces
    for x in string.punctuation:
        new = new.replace(x,"")
        new = new.replace('\n', ' ')
    pos = -1
    while pos != len(new):
        nextpos = new.find(' ', pos+1, len(new))
        words.append(new[pos+1:nextpos])
        pos = new.find(' ', pos+1, len(new))
        
    
    infile.close()
    outfile.close()

except IOError:
        print("Error reading MYSTERY.IN or writing to RESULT.OUT")

# remove all punctuations
# convert to upper/lower case
# add all words to list
# remove non-significant words (eg articles, pronouns, etc.)
# compute frequencies of remaining words
# analyse top 3 most frequent words
