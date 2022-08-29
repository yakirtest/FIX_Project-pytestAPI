



import json


class Pet_store_base:

    def to_json(self) -> str:
        result = dict()
        for key, val in self.__dict__.items():
            if val is not None:
                # if key.startswith('_'):
                    result[key[1:]] = val
                #     result[key] = val
        return result

    def __str__(self) -> str:
        return json.dumps(self.to_json())