import requests
import pandas as pd

# Fonction pour récupérer les données JSON d'une page spécifique, tout en ignorant les erreurs
def fetch_products_from_page(page_number):
    try:
        url = f'https://world.openfoodfacts.org/cgi/search.pl?search_simple=1&action=process&json=1&page={page_number}'
        response = requests.get(url)
        
        # Si la requête est réussie (code 200), on récupère les produits
        if response.status_code == 200:
            return response.json()['products']
        else:
            print(f"Erreur lors de la récupération de la page {page_number}: {response.status_code}")
            return []  # Retourne une liste vide si la page ne peut pas être récupérée
    except Exception as e:
        print(f"Exception rencontrée pour la page {page_number}: {e}")
        return []  # Retourne une liste vide si une exception est rencontrée