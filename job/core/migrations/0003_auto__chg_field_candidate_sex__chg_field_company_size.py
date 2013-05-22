# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Candidate.sex'
        db.alter_column(u'core_candidate', 'sex', self.gf('django.db.models.fields.CharField')(max_length=12))

        # Changing field 'Company.size'
        db.alter_column(u'core_company', 'size', self.gf('django.db.models.fields.CharField')(max_length=10))

    def backwards(self, orm):

        # Changing field 'Candidate.sex'
        db.alter_column(u'core_candidate', 'sex', self.gf('django.db.models.fields.CharField')(max_length=2))

        # Changing field 'Company.size'
        db.alter_column(u'core_company', 'size', self.gf('django.db.models.fields.CharField')(max_length=2))

    models = {
        u'core.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            'education': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'experience': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'more_info': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '24'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'MAN'", 'max_length': '12'})
        },
        u'core.company': {
            'Meta': {'object_name': 'Company'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '24'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '10'})
        }
    }

    complete_apps = ['core']