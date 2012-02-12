from art.models import ArtObject
from django.contrib import admin

# admin.site.register(ArtObject)

class ArtObjectAdmin(admin.ModelAdmin):
  list_display = ('title', 'technique', 'dimensions')
  search_fields = ['title']

admin.site.register(ArtObject, ArtObjectAdmin)