'''
Playground for phonetics.py imports
'''

import phonetics as ph

while True:
    word = input('Enter word to fetch phoentics:\t')
    print(ph.ipa_fd(word))

