import json

from models import Author, Quote

file_name = './task1/src/qoutes.json'


if __name__ == "__main__":
    with open(file_name, 'r') as file:
        qoutes = json.load(file)
    if qoutes:
        for qoute in qoutes:
            try:
                Quote(
                    author = Author.objects(fullname=qoute.get('author'))[0],
                    quote_ = qoute.get('quote'),
                    tags = qoute.get('tags'),
                ).save()
            except:
                print('The data do not fit the model')
