# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Column', fields ['slug']
        db.create_unique('columns_column', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Column', fields ['slug']
        db.delete_unique('columns_column', ['slug'])


    models = {
        'columns.column': {
            'Meta': {'object_name': 'Column'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['columns']