#!/bin/bash
# Création d'un environnement virtuel pour Python 3

# Détection du système d'exploitation
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    VIRTUALENV_COMMAND="virtualenv -p python3"
    ACTIVATE_COMMAND="source env/bin/activate"
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
    # Linux
    VIRTUALENV_COMMAND="virtualenv -p python3"
    ACTIVATE_COMMAND="source env/bin/activate"
elif [[ "$OSTYPE" == "msys" ]]; then
    # Windows (Git Bash)
    VIRTUALENV_COMMAND="virtualenv -p python3"
    ACTIVATE_COMMAND="source env/Scripts/activate"
else
    echo "Système d'exploitation non pris en charge"
    exit 1
fi

# Crée le répertoire "env" pour cet environnement
$VIRTUALENV_COMMAND env

# Active cet environnement
$ACTIVATE_COMMAND

# Installe les dépendances en utilisant le fichier requirements.txt
pip3 install -r requirements.txt
