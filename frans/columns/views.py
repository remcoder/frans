from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
from django.http import Http404

from columns.models import Column

def index(request):
    all_columns = [c for c in Column.objects.all()]
    column = all_columns[0] # FIXME: get latest column if no specific one is requested
    #print column
    
    return render_to_response('columns/index.html', \
      { 
        'column': column,
        'all_columns' : all_columns
      })

def by_slug(request, slug=None):
  if slug == None:
    return self.index(request)

  print "slug: " + slug
  all_columns = [c for c in Column.objects.all()]
  column = filter(lambda c: c.slug == slug,  all_columns)
  print column
  
  if not column:
    raise Http404

  return render_to_response('columns/index.html', \
    { 
      'column': column[0],
      'all_columns' : all_columns
    })