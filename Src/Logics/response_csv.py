from Src.Core.abstract_response import abstract_response
from Src.Core.common import common

class response_scv(abstract_response):

    def build(self, format: str, data: list):
        text = ""
        if len(data) == 0:
            return text
        fields = common.get_fields(data[0])
        text += ";".join(fields) + "\n"
        for item in data:
            values = [str(getattr(item, f)) for f in fields]
            text += ";".join(values) + "\n"

        return text
