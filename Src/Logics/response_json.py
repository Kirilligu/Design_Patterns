from Src.Core.abstract_response import abstract_response
import json
from Src.Core.common import common

class response_json(abstract_response):
    def build(self, format: str, data: list):
        result = []
        for item in data:
            obj = {}
            for field in common.get_fields(item):
                obj[field] = getattr(item, field)
            result.append(obj)
        return json.dumps(result, ensure_ascii=False, indent=2)
