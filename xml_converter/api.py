from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from xml_converter.serializers.ConvertXMLToJsonSerializer import ConvertXMLToJsonSerializer


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        data = {'file': request.FILES['file']}
        serializer = ConvertXMLToJsonSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
