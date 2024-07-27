# Write your solution here
# .strip() .rstrip() .lstrip() - removes all spaces, line breaks, tabs and other characters from the beginning and end of a string
# .replace('\n', '')
# .split(';') - takes separator - return a list of strings, separated at the separator.

def prepare_list(filename):
    recipe_list = []
    with open(filename) as recipes:
        for w in recipes.read().split('\n\n'):
            recipe_list.append(w.split('\n'))
    return recipe_list


def search_by_name(filename: str, word: str):
    recipe_list = prepare_list(filename)
    
    found_names = []
    for i in recipe_list:
        if word.lower() in i[0].lower():
            found_names.append(i[0]) 
    return found_names


def search_by_time(filename: str, prep_time: int):
    recipe_list = prepare_list(filename)
    prep_list = []
    for i in recipe_list:
        if int(i[1]) <= prep_time:
            prep_list.append(i[0]+', preparation time '+i[1]+' min')
    return prep_list

def search_by_ingredient(filename: str, ingredient: str):
    recipe_list = prepare_list(filename)
    ingr = []
    for i in recipe_list:
        if ingredient in i[2:]:
            ingr.append(i[0]+', preparation time '+i[1]+' min')
    return ingr


if __name__ == "__main__":
    prepare_list()
    search_by_name()
    search_by_time()
    search_by_ingredient()