# arborescence_util.py
import os
import sys
import json
import re
from loguru import logger
import yaml

file_identifier = "File"


def dessiner_arborescence(dossier, prefixe="", ignore_dossiers=None, ignore_regex=None):
    # Récupérer la liste des éléments dans le dossier
    elements = os.listdir(dossier)

    # Parcourir les éléments
    for i, element in enumerate(elements):
        chemin_complet = os.path.join(dossier, element)
        est_dernier = i == len(elements) - 1

        # Ignorer les dossiers spécifiés
        if ignore_dossiers and element in ignore_dossiers:
            continue

        # Ignorer les dossiers correspondant au motif regex
        if ignore_regex and re.match(ignore_regex, element):
            continue

        # Afficher le préfixe
        if est_dernier:
            print(prefixe + "└── " + element)
        else:
            print(prefixe + "├── " + element)

        # Si l'élément est un dossier, récursivement afficher son contenu
        if os.path.isdir(chemin_complet):
            nouveau_prefixe = prefixe + ("    " if est_dernier else "│   ")
            dessiner_arborescence(chemin_complet, nouveau_prefixe, ignore_dossiers, ignore_regex)

def afficher_arborescence_format(chemin_dossier, format, ignore_dossiers=None, ignore_regex=None):
    if format == "json":
        arborescence_json = generer_arborescence_json(chemin_dossier, ignore_dossiers, ignore_regex)
        print(json.dumps(arborescence_json, indent=2))
    elif format == "yaml":
        arborescence_yaml = generer_arborescence_yaml(chemin_dossier, ignore_dossiers, ignore_regex)
        print(yaml.dump(arborescence_yaml, default_flow_style=False))

def generer_arborescence_json(dossier, ignore_dossiers=None, ignore_regex=None):
    arborescence = {}
    elements = os.listdir(dossier)

    for element in elements:
        chemin_complet = os.path.join(dossier, element)

        # Ignorer les dossiers spécifiés
        if ignore_dossiers and element in ignore_dossiers:
            continue

        # Ignorer les dossiers correspondant au motif regex
        if ignore_regex and re.match(ignore_regex, element):
            continue

        if os.path.isdir(chemin_complet):
            arborescence[element] = generer_arborescence_json(chemin_complet, ignore_dossiers, ignore_regex)
        else:
            arborescence[element] = file_identifier
    logger.debug(f"📂 Arborescence JSON : {arborescence}")
    return arborescence

def generer_arborescence_yaml(dossier, ignore_dossiers=None, ignore_regex=None):
    arborescence = {}
    elements = os.listdir(dossier)

    for element in elements:
        chemin_complet = os.path.join(dossier, element)

        # Ignorer les dossiers spécifiés
        if ignore_dossiers and element in ignore_dossiers:
            continue

        # Ignorer les dossiers correspondant au motif regex
        if ignore_regex and re.match(ignore_regex, element):
            continue

        if os.path.isdir(chemin_complet):
            arborescence[element] = generer_arborescence_yaml(chemin_complet, ignore_dossiers, ignore_regex)
        else:
            arborescence[element] = file_identifier
    # log directly into the logfil without printing to the console
    logger.debug(f"📂 Arborescence YAML : {arborescence}")
    return arborescence

def creer_arborescence(description_json, chemin_dossier, ignore_dossiers=None, ignore_regex=None):
    try:
        # Charger la description JSON
        with open(description_json, 'r') as file:
            description = json.load(file)
            logger.debug(f"📂 Description to Create: {description}")

        # Créer l'arborescence
        for nom, contenu in description.items():
            # Ignorer les dossiers spécifiés
            if ignore_dossiers and nom in ignore_dossiers:
                continue

            # Ignorer les dossiers correspondant au motif regex
            if ignore_regex and re.match(ignore_regex, nom):
                continue

            chemin_element = os.path.join(chemin_dossier, nom)

            if isinstance(contenu, dict):
                # Si la valeur est un dictionnaire, récursivement créer le dossier
                os.makedirs(chemin_element, exist_ok=True)
                logger.info(f"📂 Dossier créé : {chemin_element}")
                creer_arborescence(description[nom], chemin_element, ignore_dossiers, ignore_regex)
            elif contenu == "File":
                # Si la valeur est "File", créer le fichier
                with open(chemin_element, 'w') as file:
                    file.write("")  # Vous pouvez ajouter du contenu si nécessaire
                logger.info(f"✅ Fichier créé : {chemin_element}")
            else:
                logger.warning(f"⚠️ Valeur non reconnue pour {nom} : {contenu}")

        logger.info("✅ Arborescence créée avec succès à partir de la description JSON.")

    except Exception as e:
        logger.error(f"❌ Une erreur s'est produite lors de la création de l'arborescence : {e}")