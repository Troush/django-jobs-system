# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Candidate', fields ['name']
        db.create_index(u'core_candidate', ['name'])

        # Adding index on 'Candidate', fields ['position']
        db.create_index(u'core_candidate', ['position'])

        # Adding unique constraint on 'Candidate', fields ['email']
        db.create_unique(u'core_candidate', ['email'])

        # Adding index on 'Company', fields ['name']
        db.create_index(u'core_company', ['name'])

        # Adding unique constraint on 'Company', fields ['name']
        db.create_unique(u'core_company', ['name'])

        # Adding index on 'Company', fields ['email']
        db.create_index(u'core_company', ['email'])

        # Adding unique constraint on 'Company', fields ['email']
        db.create_unique(u'core_company', ['email'])

        # Adding index on 'Company', fields ['size']
        db.create_index(u'core_company', ['size'])


    def backwards(self, orm):
        # Removing index on 'Company', fields ['size']
        db.delete_index(u'core_company', ['size'])

        # Removing unique constraint on 'Company', fields ['email']
        db.delete_unique(u'core_company', ['email'])

        # Removing index on 'Company', fields ['email']
        db.delete_index(u'core_company', ['email'])

        # Removing unique constraint on 'Company', fields ['name']
        db.delete_unique(u'core_company', ['name'])

        # Removing index on 'Company', fields ['name']
        db.delete_index(u'core_company', ['name'])

        # Removing unique constraint on 'Candidate', fields ['email']
        db.delete_unique(u'core_candidate', ['email'])

        # Removing index on 'Candidate', fields ['position']
        db.delete_index(u'core_candidate', ['position'])

        # Removing index on 'Candidate', fields ['name']
        db.delete_index(u'core_candidate', ['name'])


    models = {
        u'core.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            'education': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'experience': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'more_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_index': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_index': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'MAN'", 'max_length': '12'})
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