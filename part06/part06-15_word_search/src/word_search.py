# Write your solution here
import re

def find_words(search_term: str) -> list:
    with open("words.txt", 'r') as file:
        word_list = [line.strip() for line in file]

    if search_term.startswith('*'):
        return [word for word in word_list if word.endswith(search_term[1:])]
    
    elif search_term.endswith('*'):
        return [word for word in word_list if word.startswith(search_term[:-1])]
    
    elif '.' in search_term:
        pattern = re.compile(search_term)
        return [word for word in word_list if pattern.fullmatch(word)]
    
    else:
        return [word for word in word_list if word == search_term]

if __name__ == "__main__":
    print(find_words("cat"))
