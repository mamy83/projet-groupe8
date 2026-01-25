# SolarGuard – Optimiseur de consommation solaire

SolarGuard est une application web conçue pour aider les utilisateurs d'installations solaires à gérer efficacement l'énergie stockée dans leurs batteries. Grâce à un algorithme intelligent, l'application analyse la charge actuelle et conseille l'usage des appareils pour maximiser l'autonomie et préserver la durée de vie des batteries.

## Fonctionnalités Clés

- **Tableau de Bord Dynamique** : Visualisez l'état de votre batterie, l'autonomie restante et l'historique de charge.
- **Algorithme de Conseil** : Recevez des recommandations personnalisées (Optimal, Vigilance, Critique) selon votre niveau d'énergie.
- **Gestion d'Appareils** : Gérez vos équipements électriques par puissance et priorité (critique vs confort).
- **Configuration Système** : Paramétrez les détails techniques de votre installation (Ah, Watts, Tension).

## Prérequis

- **Python** : Version 3.10 ou supérieure recommandée.
- **Navigateur Web** : Chrome, Firefox, Edge ou Safari (recommandé pour une meilleure expérience responsive).

## Installation

### 1. Cloner le projet
```bash
git clone <url-du-depot>
cd projet
```

### 2. Créer un environnement virtuel
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations
```bash
python manage.py migrate
```

## Lancement du Projet

Pour démarrer le serveur de développement local :
```bash
python manage.py runserver
```
Une fois le serveur lancé, accédez au site via : `http://127.0.0.1:8000/`

## Configuration Initiale

1. **Compte** : Créez un compte utilisateur.
2. **Système** : Une fois connecté, rendez-vous dans la section "Configuration" pour entrer les caractéristiques de votre installation solaire.
3. **Appareils** : Ajoutez vos appareils électriques habituels avec leur puissance en Watts.
4. **Usage** : Utilisez le bouton "Input Niveau" pour mettre à jour votre niveau de batterie actuel et voir l'algorithme en action !

---
*Projet réalisé pour optimiser l'autonomie énergétique solaire.*
