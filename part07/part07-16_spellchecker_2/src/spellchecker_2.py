# Write your solution here
from difflib import get_close_matches

def correct():
    word_list = []
    with open("wordlist.txt") as correct_words:
        for word in correct_words:

            word_list.append(word.strip().lower())
    return word_list

def suggestions(word: str, word_list: list):
    print("suggestions:")
    print(f"{word}: {', '.join(get_close_matches(word, word_list))}")

def main():
    word_list = correct()
    user_input = input("write text: ")
    spell_checked = ""
    misspell = []
    for word in user_input.split():
        if word.lower() not in word_list:
            misspell.append(word)
            word = "*"+word+"*"
        spell_checked += word+' '
    print(spell_checked)
    for i in misspell:
        suggestions(i, word_list)

main()