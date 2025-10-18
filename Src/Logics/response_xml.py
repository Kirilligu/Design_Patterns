from Src.Core.abstract_response import abstract_response
from Src.Core.common import common

class response_xml(abstract_response):
    def build(self, format: str, data: list):
        text = "<root>\n"
        for item in data:
            text += "  <item>\n"
            for field in common.get_fields(item):
                text += f"    <{field}>{getattr(item, field)}</{field}>\n"
            text += "  </item>\n"
        text += "</root>"
        return text
