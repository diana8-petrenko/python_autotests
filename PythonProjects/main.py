import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '48981cc183ebfed0a38b2473c61fffd3'
HEADER = {'Content-Type: application/json', 'trainer_token': TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "bikbulatova00@list.ru",
    "password": "HelloDish1"
}

body_conformation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response.conformation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_conformation)
print(response_conformation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_conformation)
print(response_create.status_code)

pokemon_id = response_create.json()['id']