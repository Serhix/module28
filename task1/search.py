from connect_redis import cache
from models import Author, Quote


def parse_input(input_text: str):
    action = None
    search_value = None
    if input_text.startswith('exit'):
        action = 'exit'
        return action, 
    else: 
        try:
            action = input_text.split(':')[0]
            search_value = [val.strip() for val in input_text.split(':')[1].split(',')]
        except:
            print('Incorect comand')
    return action, search_value

@cache
def get_quote_by_name(name: str):
    authors = []
    for author in Author.objects.all():
        if author.fullname.lower().startswith(name.lower()):
            authors.append(author)
    result = Quote.objects(author = authors[0])
    quote_to_cache = []
    for quote in result:
        quote_to_cache.append(quote.quote_.encode("utf-8"))
    return quote_to_cache

@cache
def get_quote_by_tag(pars_tag: str):
    result = Quote.objects.all()
    quote_to_cache = []
    for quote in result:
        for tag in quote.tags:
            if tag.lower().startswith(pars_tag.lower()):
                quote_to_cache.append(quote.quote_.encode("utf-8"))
    return set(quote_to_cache)


def get_quote_by_tags(pars_tags: list):
    result = Quote.objects.all()
    quote_results = []
    for quote in result:
        for tag in quote.tags:
            for pars_tag in pars_tags:   
                if tag.lower().startswith(pars_tag.lower()):
                    quote_results.append(quote.quote_.encode("utf-8"))
    return set(quote_results)
    
        
def main():
    while True:
        comand = input('>> ')
        action = parse_input(comand)[0]
        match action:
            case 'name':
                print(*get_quote_by_name(parse_input(comand)[1][0]))
            case 'tag':
                print(*get_quote_by_tag(parse_input(comand)[1][0]))
            case 'tags':
                print(*get_quote_by_tags(parse_input(comand)[1]))
            case 'exit':
                break
            case _:
                print('Incorect comand')
    

if __name__ == '__main__':
    main()