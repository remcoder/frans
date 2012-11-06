from columns.models import Column
from django.contrib import admin

# admin.site.register(ArtObject)

class ColumnAdmin(admin.ModelAdmin):
  list_display = 'title', 'slug'
  search_fields = ['title']
  exclude = 'slug',

admin.site.register(Column, ColumnAdmin)