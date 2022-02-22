from django.http import JsonResponse
from django.shortcuts import render

from xml_converter.serializers.ConvertXMLToJsonSerializer import ConvertXMLToJsonSerializer


def upload_page(request):
    if request.method == 'POST':
        data = {'file': request.FILES['file']}
        serializer = ConvertXMLToJsonSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return JsonResponse(serializer.data)

    return render(request, "upload_page.html")
