#!/usr/bin/env python3

#take an english word that starts with a consonant, move the consonant to the end and add "ay"
#if word begins with a vowel simply add "way" to the end of the word

consonants = "aAeEiIoOuU"
vowels = "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ"

def process_word(word):
    """Function that takes in a word to translate into pig latin."""
    for char in word:
        if char == word[0] and char in consonants:
            word = word + word[0].lower() + "ay"
        elif char == word[0] and char in vowels:
            word = word + "way"
    return word


def process_sentence(sentence):
    """Function that outputs a translated list of words."""
    sentence_lst = sentence.split() #this does not get touched
    processed_sentence = [process_word(word) for word in sentence_lst]
    return " ".join(processed_sentence)




def main():
    while True:
        print("---Pig Latin translator---")
        choice = input("Would you like a word, or a sentence?")
        if choice.lower() == "sentence":
            sentence = input("Please input your sentence: \n")
            result = process_sentence(sentence)
            print(result)
        elif choice.lower() == "word":
            word = input("Please input your word: ")
            result = process_word(word)
            print(result)
        attempt = input("Try again? Y/N \n")
        if attempt.lower() == "n":
            break



if __name__ == "__main__":
    main()

