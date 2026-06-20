"""
Configuration des logs pour le projet Books to Scrape.

Ce module configure un fichier de log daté afin de tracer :
- les actions d'extraction ;
- les catégories traitées ;
- les erreurs rencontrées.
"""

import logging  # Module standard de journalisation.
from datetime import datetime  # Permet de générer une date et une heure.
from pathlib import Path  # Permet de gérer les chemins de fichiers.


def setup_logger():
    """
    Configure le système de logs du programme.

    Le fichier de log est créé dans le dossier logs avec un nom contenant
    la date et l'heure de lancement du programme.

    Returns:
        logging.Logger: Logger configuré pour le projet.
    """
    logs_dir = Path.cwd() / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = logs_dir / f"extraction_{timestamp}.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
    )

    logger = logging.getLogger("books_scraper")

    logger.info("Démarrage du programme d'extraction")
    logger.info("Fichier de log : %s", log_file)

    return logger, log_file