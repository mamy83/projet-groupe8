# ☀️ SolarGuard – Optimiseur d'Énergie Solaire Intelligent

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0%2B-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**SolarGuard** est une solution web premium conçue pour maximiser l'autonomie des installations solaires résidentielles. Grâce à des algorithmes de prédiction intelligents et une interface visuelle de pointe, gérez votre énergie comme un expert.

![Aperçu Dashboard](static/images/solar_algorithm_dashboard_1770635462363.png)

---

## ✨ Points Forts

### 🚀 Design Premium & Expérience Utilisateur
- **Landing Page Immersive** : Navigation fluide, carrousels dynamiques et animations d'entrée élégantes.
- **Interface Réactive** : Entièrement optimisée pour mobile, tablette et desktop.
- **Animations Subtiles** : Fond dot-pattern animé en continu et transitions de cartes fluides pour une sensation de modernité.

### 📊 Tableau de Bord Analytique (ApexCharts)
- **Visualisation Temps Réel** : Jauge radiale animée pour le niveau de batterie actuel.
- **Historique Prédictif** : Graphique d'aire illustrant l'évolution de votre charge sur les dernières 24h.
- **Distribution Énergétique** : Analyse de la répartition de consommation par appareil via un graphique donut.

### 🧠 Algorithme de Conseil Intelligent
- **Priorisation Automatique** : Classification des appareils en "Recommandé", "Acceptable" ou "À éviter" selon l'état de la batterie.
- **Calcul d'Autonomie** : Estimation précise du temps restant basée sur votre consommation actuelle.
- **Modes de Vigilance** : Seuils critiques (20%) et optimaux (80%) pour préserver la santé de vos batteries.

---

## 🛠️ Stack Technique

- **Backend** : Django (Python) pour la robustesse et la sécurité.
- **Frontend** : CSS3 moderne (Variables, Keyframes, Flexbox/Grid) & JavaScript Vanilla.
- **Visualisation** : ApexCharts.js pour des graphiques animés haute performance.
- **Iconographie** : Phosphor Icons pour un look épuré.
- **Authentification** : Système sécurisé basé sur l'email, conforme aux standards modernes.

---

## 📸 Captures d'Écran

| Gestion des Appareils | Monitoring Intelligent |
| :---: | :---: |
| ![Appareils](static/images/smart_appliances_control_1770635728381.png) | ![Batterie](static/images/solar_battery_dashboard_1770635840297.png) |

---

## 🚀 Installation & Lancement

### 1. Clonage & Environnement
```bash
git clone https://github.com/mamy83/projet-groupe8.git
cd projet-groupe8
python -m venv .venv
.\.venv\Scripts\activate  # Windows
```

### 2. Dépendances & Base de données
```bash
pip install -r requirements.txt
python manage.py migrate
```

### 3. Exécution
```bash
python manage.py runserver
```

---

## 📖 Utilisation

1. **Configuration Initiale** : Dans la page "Configuration", renseignez la capacité de vos batteries (Ah) et la puissance de vos panneaux (Wc).
2. **Inventaire** : Ajoutez vos appareils (TV, Frigo, Lampe...) avec leur puissance moyenne.
3. **Suivi** : Mettez à jour votre niveau de batterie via "Input Niveau" pour recevoir vos conseils immédiats.

---

## 🤝 Contribution

Réalisé par l'équipe **SolarGuard (Groupe 8)**.
N'hésitez pas à ouvrir une *Issue* ou à soumettre une *Pull Request* !

*Optimisé pour un avenir plus vert.* 🌱
