# Utiliser une image Python de base
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances et installer les bibliothèques Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code du projet dans le conteneur
COPY . /app

# Exposer le port de l'application Flask
EXPOSE 5000

# Définir une variable d'environnement pour signaler l'exécution dans Docker
ENV FLASK_RUN_IN_DOCKER=1

# Commande pour lancer l'application
CMD ["python", "run.py"]
