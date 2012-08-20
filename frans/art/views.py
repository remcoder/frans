from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
from art.models import ArtObject

def index(request):
    artObjects = [ao for ao in ArtObject.objects.all()]
    json_serializer = serializers.get_serializer("json")()
    jsonArtObjects = json_serializer.serialize(artObjects, \
      ensure_ascii=False)
    return render_to_response('art/index.html', \
      { 'artObjects': jsonArtObjects })