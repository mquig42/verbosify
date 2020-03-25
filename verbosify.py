################################################################################
# verbosify.py
# 2020-03-24
# Mike Quigley
#
# It's the amazing word elongator. Runs every word of its input through a
# thesaurus, replaces it with longest synonym. Type 'exit' to quit.
#
# Inspired by a forum post that appears to have been using a similar approach.
################################################################################

from nltk.corpus import wordnet

def elongate(word):
    if len(word) == 1:
        return word
    longest = word
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            if len(lm.name()) > len(longest) and lm.name().count('_') == 0:
                longest = lm.name()
    return longest

s = 'text'
while s != 'exit':
    s = input('> ')
    words = s.split()
    out = ''
    for word in words:
        out += elongate(word) + ' '
    print(out)
