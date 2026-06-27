import json



def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def load_html_template(filepath):
    """Loads data from the html file """
    with open(filepath, "r") as handle:
        return handle.read()

def get_information(animals_data):
    """gets information about name, nutrition, forst place from location list, type"""
    output = ""

    for animals in animals_data:
        output += '<li class="cards__item">'

        if "name" in animals.keys():
            output += f"Name: {animals['name']}<br/>\n"
        if "diet" in animals['characteristics'].keys():
            output += f"Diet: {animals['characteristics']['diet']}<br/>\n"
        if "locations" in animals.keys():
            output += f"Location: {animals['locations'][0]}<br/>\n"
        if 'type' in animals['characteristics']:
            output += f"Type: {animals['characteristics']['type']}<br/>\n"
        output += '</li>'

    return output


animals_data = load_data("animals_data.json")

html_template = load_html_template("animals_template.html")

output = get_information(animals_data)

html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

def create_html():
    with open("animals.html", "w") as file:
        file.write(html)
create_html()