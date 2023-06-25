import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(soup, quotes):
    # récupérer tous les éléments de la <div> sur la page
    quote_elements = soup.find_all('div', class_='result')
    # iterating over the list of quote elements
    # to extract the data of interest and store it
    # in quotes
    for quote_element in quote_elements:
        # extraire le texte
        resto = quote_element.find('span').text
        rue = quote_element.find('div', class_='street-address').text
        ville = quote_element.find('div', class_='locality').text
        num_tel=quote_element.find('div', class_='phones phone primary').text
        # Ajoute chaque element a la liste
        restos_NY.append(
            {
                'resto': resto,
                'rue': rue,
                'ville': ville,
                'num_tel' : num_tel

            }
        )

# l'URL du site
base_url = 'https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New+York%2C+NY'

# definir le user agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# récupération de la page Web cible
page = requests.get(base_url, headers=headers)

# analyser la page Web cible avec Beautiful Soup
soup = BeautifulSoup(page.text, 'html.parser')

#liste pour stoquer nos données
restos_NY = []

# scraping the home page
scrape_page(soup, restos_NY)

# overture du fichier csv en mode ecriture
csv_file = open('restos_NY', 'w', encoding='utf-8', newline='')

# initialisation du fichier pour insérer des données
# dans le fichier CSV
writer = csv.writer(csv_file)

# creation des champs du fichier csv
writer.writerow(['resto','rue','ville','num'])

# ajouter les données récuperé
for quote in restos_NY:
    writer.writerow(quote.values())

# fermeture du fichier csv
csv_file.close()