"""App configuration."""
from os import environ


class Config:
    """Set configuration vars from .env file."""

    # General Config
    DATABASE = environ.get('DATABASE')
    DB_DRIVER = environ.get('DB_DRIVER')
    DB_USER = environ.get('DB_USER')
