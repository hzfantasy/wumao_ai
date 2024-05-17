import configparser
from singleton import SingletonMeta


class Config(metaclass=SingletonMeta):
    def __init__(self):
        self._config_parser = configparser.ConfigParser()
        self._config_parser.read(filenames="./config.ini", encoding="utf8")
        self.kimi_config = self._config_parser["kimi"]

    def __new__(cls, *args, **kwargs):
        return super(Config, cls).__new__(cls)

    @property
    def kimi_token(self):
        return self.kimi_config.get("api_key")


config = Config()
