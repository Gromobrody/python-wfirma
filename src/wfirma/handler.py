from abc import ABC


class BaseHandler(ABC):
    access_key: str
    secret_key: str
    app_key: str


class WFirmaHandler(BaseHandler): ...


class AsyncWFirmaHandler(BaseHandler): ...
