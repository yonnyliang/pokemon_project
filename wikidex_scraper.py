import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

pokedex = []

response = requests.get('https://www.wikidex.net/wiki/Lista_de_Pok%C3%A9mon_con_sus_caracter%C3%ADsticas_base')

soup = BeautifulSoup(response.content, 'html.parser')

pokedex_table = soup.find('table')

for pokemon in pokedex_table.find_all("tr"):
    pokemon_cell = []
    for cell in pokemon.find_all('td'):
        pokemon_cell.append(cell.text)
    pokedex.append(pokemon_cell)

df = pd.DataFrame(pokedex)

print(df)
#df.to_csv('pokemon_stats_dataset.csv', encoding='utf-8')
