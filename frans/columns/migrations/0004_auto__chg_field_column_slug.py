# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Column.slug'
        db.alter_column('columns_column', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Column.slug'
        db.alter_column('columns_column', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    models = {
        'columns.column': {
            'Meta': {'object_name': 'Column'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['columns']