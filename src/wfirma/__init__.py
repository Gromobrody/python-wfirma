"""wFirma."""


class WFirmaBase:
    def __init__(self, access_key, secret_key, app_key, company_id):
        self.url = "https://api2.wfirma.pl/"

        self.headers = {
            "accessKey": access_key,
            "secretKey": secret_key,
            "appKey": app_key,
        }
        self.params = {
            "outputFormat": "xml",
            "inputFormat": "xml",
            "company_id": company_id,
        }


class Wfirma(WFirmaBase): ...


class AsyncWfirma(WFirmaBase): ...
