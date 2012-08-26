from homepage.models import HomepagePhoto
from django.contrib import admin

# admin.site.register(ArtObject)

class HomepageAdmin(admin.ModelAdmin):
  list_display = ('title', 'image')
  search_fields = ['title']

admin.site.register(HomepagePhoto, HomepageAdmin)