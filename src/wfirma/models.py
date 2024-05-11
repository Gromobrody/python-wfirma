from pydantic_xml import BaseXmlModel


class WModel(BaseXmlModel, search_mode="unordered"):
    pass


class ResponseParams(WModel):
    limit: int
    page: int
    total: int


class ItemBase(WModel):
    parameters: ResponseParams


class ResponseStatus(WModel):
    code: str


class ResponseBase(WModel):
    status: ResponseStatus
