from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
from homepage.models import HomepagePhoto

def index(request):
    photos = [p for p in HomepagePhoto.objects.all()]
    json_serializer = serializers.get_serializer("json")()
    jsonPhotos = json_serializer.serialize(photos, ensure_ascii=False)
    return render_to_response('homepage/index.html', { 'images': jsonPhotos })