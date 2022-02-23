import xmltodict
from rest_framework import serializers
import json


class CustomFileField(serializers.FileField):

    def to_representation(self, data):
        obj = xmltodict.parse(data)
        data_json = json.loads(json.dumps(obj))
        root = data_json and list(data_json.keys())[0]
        if root:
            root_data = self._transform(data_json[root]) or ''
            return {root: root_data}

        return root

    def _transform(self, data):
        if isinstance(data, dict):
            res = []
            for k, v in data.items():
                if isinstance(v, list):
                    res.extend([{k: self._transform(item)} for item in v])
                elif isinstance(v, dict):
                    res.append({k: self._transform(v)})
                else:
                    res.append({k: v if v else ''})

            data = res

        elif isinstance(data, list):
            data = [self._transform(item) for item in data]

        return data


class ConvertXMLToJsonSerializer(serializers.Serializer):
    file = CustomFileField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data['file']
