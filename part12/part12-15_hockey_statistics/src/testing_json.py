import json
def load_data(file_name):
    with open(file_name) as file:
        return json.load(file)

x = load_data("p.json")
