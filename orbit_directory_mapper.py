# arborescence.py
import os
from loguru import logger
import argparse
import sys
from arborescence_util import dessiner_arborescence, creer_arborescence, afficher_arborescence_format


if __name__ == "__main__":
    # Configurer les paramètres en ligne de commande
    parser = argparse.ArgumentParser(description="Afficher ou Créer une arborescence de Dossier en Une Seconde.")
    parser.add_argument("chemin_dossier", type=str, help="Chemin du dossier à explorer ou créer")
    parser.add_argument("--ignore", type=str, nargs="*", help="Noms des dossiers à ignorer")
    parser.add_argument("--regex", type=str, help="Motif regex pour ignorer certains dossiers")
    parser.add_argument("--format", choices=["json", "yaml"], help="Format de l'arborescence (JSON ou YAML)")
    parser.add_argument("--create", action="store_true", help="Mode création d'arborescence")
    parser.add_argument("--description", type=str, help="Chemin de la description JSON pour le mode création")

    args = parser.parse_args()

    logger.remove()
    # Configurer les logs avec Loguru
    logger.add("logs/structure_dossier.log", rotation="10 MB", level="DEBUG")
    # Ajouter un autre gestionnaire pour la console, mais uniquement pour les niveaux INFO et supérieurs
    logger.add(sys.stdout, level="INFO")

    # Vérifier si le chemin existe
    if os.path.exists(args.chemin_dossier):
        logger.info("🌲 Début de l'opération 🌲")

        # Mode "Show/Draw"
        if not args.create:
            logger.info(f"📂 Structure du dossier : {args.chemin_dossier}")
            # Afficher l'arborescence dans le format spécifié
            if args.format:
                logger.info(f"📂 Affichage de l'arborescence dans le format {args.format.upper()} :\n")
                afficher_arborescence_format(args.chemin_dossier, args.format, ignore_dossiers=args.ignore, ignore_regex=args.regex)
            else:   
                dessiner_arborescence(args.chemin_dossier, ignore_dossiers=args.ignore, ignore_regex=args.regex)

        # Mode "Create"
        else:
            if args.description:
                creer_arborescence(args.description, args.chemin_dossier, ignore_dossiers=args.ignore, ignore_regex=args.regex)
            else:
                logger.error("❌ La description JSON est requise en mode création.")
    else:
        logger.error("❌ Le chemin spécifié n'existe pas.")
