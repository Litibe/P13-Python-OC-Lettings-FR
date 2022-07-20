## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
   [![Python badge](https://img.shields.io/badge/Python->=3.9-blue.svg)](https://www.python.org/)

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Litibe/P13-Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Lancement du projet en local - DOCKER 
Si vous décirez simplement utiliser le site en local sans modification du code source, un container Docker est présent sur le dockerHub pour une installation automatisée des dépendances ainsi qu'un lancement automatique en une ligne de commande.

### Pré-requis : 
  - Installation de Docker sur votre machine : 
    - [Pour Mac](https://www.docker.com/products/docker-desktop/)
    - [Pour Windows](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=header)
    - [Pour Linux](https://docs.docker.com/desktop/linux/install/)

### Lancement du script de récupération du Container avec lancement :
Attention votre application Docker doit être lancée sur votre machine puis ouvrer votre terminal.
  ```shell
   docker run -d -p 80:8000 litibe/p13_django
   ```
   Docker va : 
   - Télécharger l'image du container issue du [Docker Hub - litibe/p13_django](https://hub.docker.com/r/litibe/p13_django/tags) si l'image est non présente/correspondante à votre image présente en locale sur votre machine.
   - Exécuter le script en mode "détach", votre application Docker gère l'application plutôt que votre terminal lançant le script
   - Connecter le port 80 de votre navigateur au port 8000 du serveur Django présent dans le container
   - Aller sur `http://localhost` ou `http://127.0.0.1`
   - Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!` sur sur `http://localhost/admin/` ou `http://127.0.0.1/admin/`

NB : Est présent sur le DockerHub, la dernière image compilée et présente sur le site de production.

## DEPLOIEMENT - CIRCLECI
### Pré-requis :
Est présent à la racine du projet : 
  - .circleci/config.yml (fichier de gestion du pipeline CircleCi)
  - .env (fichier contenant les variables d'environnement)
  - db.json (fichier contenant une copie de la base de données pour migration sur Héroku, à metre à la racine du projet).
Pour la constitution du fichier de base de données, merci d'exécuter dans votre environnement virtuel de développement la commande suivante dans votre terminal : 
  ```shell
   python manage.py dumpdata > db.json
   ```
  - Dockerfile (fichier permettant la compilation du projet dans un container Docker)
  - Procfile (fichier nécessaire pour le lancement du serveur sur Heroku)

### Variable d'environnement :
A des fins de confidentialités, les données sensibles ne sont présentes dans les fichiers sources du projet.
Pour un usage local, vous devez continuer votre fichier .env avec les variables suivantes : 
  - SECRET_KEY
  - DEBUG
  - DATABASE_NAME
  - SENTRY_SDK

Pour CircleCI, dans la configuration du projet - Variables d'Environnement :

  Même chose que ci-dessus pour le fonctionnement de Django :
  - SECRET_KEY
  - DEBUG
  - DATABASE_NAME
  - SENTRY_SDK

  Pour la compilation Docker : 
  - CIRCLE_BUILD_NUM : un numero de votre choix de départ pour l'identation des N° de version pour le image_docker:0.0.CIRCLE_BUILD_NUM
  - DOCKER_HUB_USER_ID (code plateforme docker hub pour le stockage de l'image container)
  - DOCKER_HUB_PASSWORD

  Pour le deploiement sur HEROKU
  - HEROKU_API_KEY - clé authentification API pour le push sur le serveur Heroku
  - HEROKU_APP_NAME - nom de l'application accessible via : https://HEROKU_APP_NAME.herokuapp.com

  Pour les notifications sur SLACK - Facultatif
  - SLACK_ACCESS_TOKEN  - recevoir un message si deploiement ok ou en echec sur Slack
  - SLACK_DEFAULT_CHANNEL  - recevoir un message si deploiement ok ou en echec sur Slack

  ### Procédure réalisée par CircleCI - Pipeline
  - ENV-TESTS
    - Create venv and pip requirements
    - Collect static to improve warning whitenoise in pytest
    - Pytest
    - Flake8
    - manage.py check --deploy (facultatif, mais obtient les optimisations à faire sur le serveur suite à l'installation d'un certificat SSL principalement)
  
  - BUILD_DOCKER_AND_PUSH_TO_HUB
    - create .env for integration into container
    - Build Docker image
    - Publish Docker Image to Docker Hub - IMAGE_TAG="0.0.${CIRCLE_BUILD_NUM}"

  - DEPLOY HEROKU
    - heroku/install - install Heroku CLI pour commande Heroku en distancielle
    - create app Heroku if not exist (wait 2 min after deleted an app !)
    - Set Var Env into heroku
    - heroku/deploy-via-git
    - make migration db
    - install db into heroku

#### Soucis réglés pour le fonctionnement du Pipeline :
- Mise à jour de Django en 3.2.14, avec intégration DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'.
- CollectStatic pour éviter les warnings de Whitenoise durant le Pytest
- Les migrations de la bases de données (oc_lettings-Site => app lettings + profiles) ont été appliquées puis supprimées pour une intégrations parfaite sur le serveur Heroku (la base de données actuelle n'ayant plus besoin des migrations de stuctures des tables sinon erreur d'intégration des migrations sur Heroku).

## Surveillance CEP - Sentry.io
### Pré-requis :
  - Ouvrir un compte Sentry
  - Intégrer la variable d'environnement "SENTRY_SDK" au fichier .env en local ainsi que dans le projet présent sur circleci. Indiquer comme valeur, l'URL fournit par sentry uniquement. L'intégration du code est déjà présent dans le fichier settings.py/urls.py pour tester l'erreur via la page [https://HEROKU_APP_NAME.herokuapp.com/sentry-debug](https://HEROKU_APP_NAME.herokuapp.com/sentry-debug)