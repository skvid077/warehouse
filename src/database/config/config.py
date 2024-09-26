import os.path

from dotenv import dotenv_values


class DbError(Exception):
    def __str__(self):
        return 'not test'


class Settings:
    __TOKEN_TELEGRAM_BOT: str

    __DB_HOST: str
    __DB_PORT: str
    __DB_USER: str
    __DB_PASS: str
    __DB_NAME: str

    __MODE: str

    def __init__(self):
        self.__MODE = config.get('MODE')
        self.__DB_USER = config.get('DB_USER')
        self.__DB_PASS = config.get('DB_PASS')
        self.__DB_HOST = config.get('DB_HOST')
        self.__DB_PORT = config.get('DB_PORT')
        self.__DB_NAME = config.get('DB_NAME')

    @property
    def database_url(self):
        return f'mysql+aiomysql://{self.__DB_USER}:{self.__DB_PASS}@{self.__DB_HOST}:{self.__DB_PORT}/{self.__DB_NAME}'

    @property
    def mode(self):
        return self.__MODE


config = dotenv_values(os.path.join(os.path.dirname(__file__), '.env'))  # test
settings = Settings()
# assert settings.mode != 'test', 'not test'
if settings.mode != 'test':
    raise DbError
