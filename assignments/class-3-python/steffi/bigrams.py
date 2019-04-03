#!/usr/bin/python
# -*- coding: utf-8 -*-

# python bigrams.py mta.txt
import sys
import random

# print all bigrams
def main():
    # 1. learn model
    model = {}
    # skip program name
    for arg in sys.argv[1:]:
        model = allBigrams(model,arg)
    # 2. generate
    for s in range(20):
        state = 'START'
        while state != 'END':
            state = step(model, state)
        print ""
        print ""
        

def step(model, state):
    nextStates = model[state].items()
    nextState = weighted_choice(nextStates)
    if not nextState=='END':
        print nextState,
    return nextState

def weighted_choice(choices):
    total = sum(w for word, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for word, w in choices:
       if upto + w > r:
          return word#, w
       upto += w
    assert False, "Shouldn't get here"

def allBigrams(bigrams,fname):
    with open(fname) as f:
        previous = ''
        for line in f:
            for word in line.split():
                if previous == '': # first sentence!
                    bigrams = addBigram(bigrams, 'START', word)
                else: 
                    if previous.endswith(('.', '."', '.”', 
                                          '?', '?"', '?”', 
                                          '!', '!"', '!”')): # new sentence!
                        bigrams = addBigram(bigrams, previous, 'END')
                        bigrams = addBigram(bigrams, 'START', word)
                    else: # new word!
                        bigrams = addBigram(bigrams, previous, word)
                previous = word
        bigrams = addBigram(bigrams, word, 'END')
    return bigrams

def addBigram(bigrams, first, second):
    if not first in bigrams:
        bigrams[first] = {}
    if not second in bigrams[first]:
        bigrams[first][second] = 1
    else:
        bigrams[first][second] = bigrams[first][second]+1
    return bigrams
 
if __name__ == "__main__":
    main()
