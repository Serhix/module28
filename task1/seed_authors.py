from datetime import datetime
import json

from models import Author

file_name = './src/authors.json'


if __name__ == "__main__":
    with open(file_name, 'r') as file:
        autors = json.load(file)
    if autors:
        for autor in autors:
            try:
                Author(
                fullname=autor.get('fullname'),
                born_date=datetime.strptime(autor.get('born_date'), '%B %d, %Y'),
                born_location=autor.get('born_location'),
                description=autor.get('description'),
                ).save()
            except:
                print('The data do not fit the model')
