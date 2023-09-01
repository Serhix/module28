import configparser

from mongoengine import connect


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'USER')
mongo_pass = config.get('DB', 'PASS')
mongo_db_name = config.get('DB', 'DB_NAME')
mongo_damain = config.get('DB', 'DOMAIN')

connect(host=f"""mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_damain}/{mongo_db_name}?retryWrites=true&w=majority""", ssl=True)
