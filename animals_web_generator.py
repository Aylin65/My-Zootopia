import json



def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
#print(animals_data)

def get_information(animals_data):
    """gets information about name, nutrition, forst place from location list, type"""
    for animals in animals_data:
        if "name" in animals.keys():
            print(f"Name: {animals['name']}")
        if "diet" in animals['characteristics'].keys():
            print(f"Diet: {animals['characteristics']['diet']}")
        if "locations" in animals.keys():
            print(f"Location: {animals['locations'][0]}")
        if 'type' in animals['characteristics']:
            print(f"Type: {animals['characteristics']['type']}")
        print()

get_information(animals_data)