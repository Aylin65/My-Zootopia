import json



def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)


def load_html_template(filepath):
    """Loads data from the html file """
    with open(filepath, "r", encoding="utf-8") as handle:
        return handle.read()

def get_information(animals_data):
    """Creates HTML for all animal cards."""
    output = ""

    for animal in animals_data:
        output += '<li class="cards__item">\n'

        if "name" in animal:
            output += f'<div class="card__title">{animal["name"]}</div>\n'

        output += '<p class="card__text">\n'

        if "diet" in animal["characteristics"]:
            output += f'<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

        if "locations" in animal and animal["locations"]:
            output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'

        if "type" in animal["characteristics"]:
            output += f'<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

        output += "</p>\n"
        output += "</li>\n"

    return output


animals_data = load_data("animals_data.json")

html_template = load_html_template("animals_template.html")

output = get_information(animals_data)

html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

def create_html():
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html)
create_html()
