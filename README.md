# Projet Commande Vocale pour Robot Unitree Go1

Ce projet permet d'interagir avec le robot Unitree Go1 en utilisant des commandes vocales. Il utilise Whisper pour la reconnaissance vocale et MQTT pour communiquer avec le robot.

## Installation

Assurez-vous que Python 3.6 ou une version ultérieure est installé sur votre système. Clonez ce dépôt, puis installez les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

Les dépendances incluent `paho-mqtt`, `whisper`, `sounddevice`, et d'autres bibliothèques nécessaires.

## Configuration

- **MQTT Broker :** Configurez l'adresse de votre broker MQTT dans `main.py` et `mqtt_manager.py`.
- **Commandes Vocales :** Les commandes vocales actuellement supportées sont configurées dans `voice_commands.py`. Vous pouvez les modifier ou en ajouter selon vos besoins.

## Utilisation

Pour démarrer le projet, exécutez le script principal :

```bash
python main.py
```

Suivez les instructions à l'écran pour enregistrer des commandes vocales. Appuyez sur n'importe quelle touche pour commencer l'enregistrement et sur 'q' pour quitter.

## Contribuer

Les contributions à ce projet sont les bienvenues. Vous pouvez contribuer en améliorant le code, en ajoutant de nouvelles fonctionnalités ou en corrigeant des bugs.
