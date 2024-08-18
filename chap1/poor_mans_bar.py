#!/usr/bin/env python3
import string

def generate_dict():
    """Generates an empty dictionary sorted in alphabetical order."""
    alpha = list(string.ascii_lowercase)
    alpha.sort()
    dicti = {}
    for letter in alpha:
        if letter not in dicti:
            dicti[letter] = []
        else:
            raise Exception("Already exists")
    return dicti

def populate_dict(sentence):
    """Populates the dictionary with the processed sentence"""
    sentence = sentence.strip('!,.?')
    words = sentence.split()
    pm_bar = generate_dict()
    for word in words:
        for char in word:
            if char not in pm_bar and char.isalpha():
                pm_bar[char].append(char)
            elif char.isalpha():
                pm_bar[char].append(char)
            elif not char.isalpha():
                raise Exception("Only valid characters allowed.")
            
    return pm_bar
#to be completed, should process the characters of a word and then append that list towards the dictionary generated


def main():
    """Main function."""
    print("--Poor Man's Bar--")
    sentence = input("Please input your sentence: \n")
    result = populate_dict(sentence.lower())
    print(result)

if __name__ == "__main__":
    main()
