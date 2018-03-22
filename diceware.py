#!/usr/local/bin/python3
import csv
import os
import random


# loads the word list csv into a dictionary and returns it
def get_word_dict(word_list_csv):
    word_dict = {}
    with open(word_list_csv, 'r') as csvfile:
        listreader = csv.reader(csvfile, delimiter=',')
        for row in listreader:
            word_dict[row[0]] = row[1]
    return word_dict


# returns a random integer between 1 and 6, like a single die
def get_random_number():
    seed_num = os.urandom(17)
    random.seed(seed_num)
    return random.randint(1, 6)


# creates a 5 digit diceware number to look up
def get_diceware_num():
    diceware_num = ''
    i = 0
    while i < 5:
        diceware_num += str(get_random_number())
        i += 1

    return diceware_num


# gets the word associated with the 5 digit number
def get_diceware_word(word_list_csv):
    word_dict = get_word_dict(word_list_csv)
    return word_dict[get_diceware_num()]


# receives user input for the number of words
def get_num_words():
    try:
        return int(input('Number of words: '))
    except:
        return get_num_words()


# receives user input for the separator character
def get_separator():
    chars = [' ', '-']
    try:
        choice = int(input('Separator: 0 = space, 1 = dash: '))
        return chars[choice]
    except:
        return get_separator()


# asks the user for number of words and separator char and generates diceware
# password
def diceware():
    num_words = get_num_words()
    separator = get_separator()

    dirname = os.path.dirname(os.path.realpath(__file__))
    word_list_csv = '{}/diceware_list.csv'.format(dirname)
    password = ''
    for i in range(num_words):
        password += get_diceware_word(word_list_csv)
        if i < num_words - 1:
            password += separator
    return password

if __name__ == "__main__":
    print(diceware())
