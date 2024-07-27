# write your solution here

def correct():
    word_list = []
    with open("wordlist.txt") as correct_words:
        for word in correct_words:

            word_list.append(word.strip().lower())
    return word_list

def main():
    word_list = correct()
    user_input = input("Write text: ")
    spell_checked = ""
    for word in user_input.split():
        if word.lower() not in word_list:
            word = "*"+word+"*"
        spell_checked += word+' '
    print(spell_checked)

main()