from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

# General
ENV = config("ENV", cast=str, default="local")
PROJECT_NAME = config("PROJECT_NAME", cast=str, default="PROJECT NAME")
VERSION = config("VERSION", cast=str, default="1.0.0")
DEBUG = config("DEBUG", cast=bool, default=True)


# Database
MY_SQL_SERVER = config("MY_SQL_SERVER", cast=str, default="localhost")
MY_SQL_DB = config("MY_SQL_DB", cast=str, default="my_sql")
MY_SQL_PORT = config("MY_SQL_PORT", cast=str, default="3306")
MY_SQL_USER = config("MY_SQL_USER", cast=str, default="my_sql")
MY_SQL_PASSWORD = config("MY_SQL_PASSWORD", cast=Secret, default="my_sql")
DATABASE_URL = config(
  "DATABASE_URL",
  cast=DatabaseURL,
  default=f"mysql://{MY_SQL_USER}:{MY_SQL_PASSWORD}@{MY_SQL_SERVER}:{MY_SQL_PORT}/{MY_SQL_DB}"
)

