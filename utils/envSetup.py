from os import path
from pathlib import Path
import environ as __environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = __environ.Env()
__environ.Env.read_env(env_file=path.join(BASE_DIR,'.env'))

class __Environment() :

    def __init__(self) -> None:

        self.DJANGO_POSTGRES_HOST: str = None
        self.DJANGO_POSTGRES_PORT: int = None
        self.DJANGO_POSTGRES_USER: str = None
        self.DJANGO_POSTGRES_PASSWORD: str = None
        self.DJANGO_POSTGRES_DATABASE: str = None

        self.DJANGO_SUPERUSER_USERNAME: str = None
        self.DJANGO_SUPERUSER_PASSWORD: str = None
        self.DJANGO_SUPERUSER_EMAIL: str = None

        self.DEFAULT_API_PAGE_LIMIT: str = None

    def run(self):

        for k in self.__dict__.keys():
            setattr(self, k, env(k))


environment = __Environment()
environment.run()
print("Environment variables loaded.")
# TODO: test this env setup inside docker container

