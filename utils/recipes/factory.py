# from inspect import signature
from random import randint # Função que gera aleatoriedade

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR') # Defino o idioma como PortuguÊs
# print(signature(fake.random_number))


def make_recipe():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6), # Chamo o titulo
        'description': fake.sentence(nb_words=12), # Descrição
        'preparation_time': fake.random_number(digits=2, fix_len=True), # Tempo de preparação
        'preparation_time_unit': 'Minutos', # Unidade do tempo de preparação
        'servings': fake.random_number(digits=2, fix_len=True), # Quan
        'servings_unit': 'Porção', # Aqui defino a unidade 
        'preparation_steps': fake.text(3000), # Passo-a-passo
        'created_at': fake.date_time(), # Faço uma data fake
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
            
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())