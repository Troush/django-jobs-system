# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Candidate', fields ['experience']
        db.create_index(u'core_candidate', ['experience'])

        # Adding index on 'Candidate', fields ['sex']
        db.create_index(u'core_candidate', ['sex'])

        # Adding index on 'Candidate', fields ['education']
        db.create_index(u'core_candidate', ['education'])


    def backwards(self, orm):
        # Removing index on 'Candidate', fields ['education']
        db.delete_index(u'core_candidate', ['education'])

        # Removing index on 'Candidate', fields ['sex']
        db.delete_index(u'core_candidate', ['sex'])

        # Removing index on 'Candidate', fields ['experience']
        db.delete_index(u'core_candidate', ['experience'])


    models = {
        u'core.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            'education': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2', 'db_index': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'experience': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'more_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_index': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '250', 'db_index': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'MAN'", 'max_length': '12', 'db_index': 'True'})
        },
        u'core.company': {
            'Meta': {'object_name': 'Company'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '10', 'db_index': 'True'})
        }
    }

    complete_apps = ['core']