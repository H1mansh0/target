from typing import List
from secrets import choice
import copy

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    result = []
    alfa = [chr(i) for i in range(65, 91)]
    while len(result) <3:
        result += [[choice(alfa) for i in range(3)]]
    return result


def get_words(filename: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    words = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if len(line[:-1]) > 3:
                words += [line[:-1].lower()]
    if letters == []:
        return words
    result = []
    for item in words:
        check_l = []
        c_letters = copy.copy(letters)
        for ele in item:
            if (letters[4] in item) and (ele in c_letters):
                check_l += '1'
                c_letters.remove(ele)
            else:
                check_l += '0'
                break
        if '0' not in check_l:
            result += [item]
    return result



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    result = []
    while True:
        word = str(input("Введіть слово: "))
        if word == '':
            break
        result += [word]
    return result



def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
