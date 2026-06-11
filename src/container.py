from src.infrastructure.config.settings import settings


class Container:
    def __init__(self):
        self.settings = settings


container = Container()