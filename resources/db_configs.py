import os

DB_HOST = os.environ.get("SWAPI_DB_HOST", "localhost")
DB_PORT = os.environ.get("SWAPI_DB_PORT", 27017)
DB_NAME = os.environ.get("SWAPI_DB_NAME", "swapi")
