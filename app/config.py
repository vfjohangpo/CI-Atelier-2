"""Configuration de l'application — lit les variables d'environnement."""

import os


class Settings:
    """Paramètres de l'application, lus depuis l'environnement."""

    app_version: str = os.getenv("APP_VERSION", "0.1.0")
    database_url: str = os.getenv(
        "DATABASE_URL", "postgresql://user:s3cret@db:5432/app"
    )
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"


settings = Settings()
