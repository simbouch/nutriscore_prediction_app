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

# Fonction pour récupérer les données sur plusieurs pages, tout en ignorant les erreurs pour les pages manquantes
def fetch_all_products(max_pages):
    all_products_data = []
    for page in range(1, max_pages + 1):
        print(f"Récupération des données de la page {page}...")
        products = fetch_products_from_page(page)
        
        if products:  # Si des produits sont récupérés, on les ajoute à la liste
            all_products_data.extend(products)
    
    return all_products_data

# Récupérer les données de 10 pages par exemple
all_products_data = fetch_all_products(10)

# Afficher un échantillon des données récupérées
print(f"Nombre total de produits récupérés : {len(all_products_data)}")
print(all_products_data[:2])  # Affiche les 2 premiers produits pour vérification