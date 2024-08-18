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
            print("Already exists")

    return dicti

def process_words(sentence, generate_dict):
    return None #to be completed, should process the characters of a word and then append that list towards the dictionary generated


def main():
    """Main function."""
    print("--Poor Man's Bar--")
    sentence = input("Please input your sentence: \n")
    print(generate_dict())


if __name__ == "__main__":
    main()
