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
import random

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

def randomize(word):
    if len(word) == 1:
        return word
    lemmas = []
    for syn in wordnet.synsets(word):
        lemmas.extend(syn.lemmas())
    if len(lemmas):
        word = random.choice(lemmas).name().replace('_', ' ')
    return word

s = 'text'
while s != 'exit':
    print("Elongate or randomize?")
    command = input('[1. elongate | 2. randomize]> ')
    if command not in ['1', '2']:
        continue

    out = ''
    s = input('sentence> ')
    words = s.split()
    if command == '1':
        for word in words:
            out += elongate(word) + ' '
    elif command == '2':
        for word in words:
            out += randomize(word) + ' '
    else:
        print("Please input 1 or 2.")

    print(out)
