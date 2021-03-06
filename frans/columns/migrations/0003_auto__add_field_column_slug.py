# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Column.slug'
        db.add_column('columns_column', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=2, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Column.slug'
        db.delete_column('columns_column', 'slug')


    models = {
        'columns.column': {
            'Meta': {'object_name': 'Column'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['columns']