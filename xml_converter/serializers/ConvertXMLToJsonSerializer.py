import xmltodict
from rest_framework import serializers
import json


class CustomFileField(serializers.FileField):

    def to_representation(self, data):
        return self.convert_file_to_json(data)

    def convert_file_to_json(self, data):
        obj = xmltodict.parse(data)
        data_json = json.loads(json.dumps(obj))
        return {k: v if v is not None else '' for k, v in data_json.items()}


class ConvertXMLToJsonSerializer(serializers.Serializer):
    file = CustomFileField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data['file']
