from decimal import Decimal

from pydantic_xml import BaseXmlModel, element, wrapped


class WModel(BaseXmlModel, search_mode="unordered"):
    pass


class ResponseParams(WModel):
    limit: int = element()
    page: int = element()
    total: None | int = element(default=None)


class ItemBase(WModel):
    # parameters: ResponseParams = element()
    pass


class ResponseStatus(WModel):
    code: str | None = element(default=None)


class VatCode(WModel, tag="vat_code"):
    id: int = element()


class WModel(BaseXmlModel, search_mode="unordered"):
    pass


class Good(ItemBase, tag="good"):
    id: str | None = element(default=None)
    name: str | None = element(default=None)
    code: str | None = element(default=None)
    unit: str | None = element(default=None)
    netto: Decimal | None = element(default=None)
    brutto: Decimal | None = element(default=None)
    gtu: str | None = element(default=None)
    lumpcode: str | None = element(default=None)
    type: str | None = element(default=None)
    classification: str | None = element(default=None)
    discount: bool | None = element(default=None)
    description: str | None = element(default=None)
    notes: int | None = element(default=None)
    documents: int | None = element(default=None)
    warehouse_type: str | None = element(default=None)
    count: int | None = element(default=None)


class ResponseBase(WModel, tag="api"):
    status: ResponseStatus | None = element(default=None)


class GoodsResponse(ResponseBase):
    items: list[Good] = wrapped("goods", element(tag="good"))
    parameters: ResponseParams = element()
