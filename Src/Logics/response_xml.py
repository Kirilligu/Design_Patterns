from Src.Core.abstract_response import abstract_response
from Src.Core.common import common

class response_xml(abstract_response):
    def build(self, format: str, data: list):
        text = '<?xml version="1.0" encoding="UTF-8"?>\n'
        text += "<root>\n"
        for item in data:
            text += "  <item>\n"
            for field in common.get_fields(item):
                text += f"    <{field}>{getattr(item, field)}</{field}>\n"
            text += "  </item>\n"
        text += "</root>"
        return text
