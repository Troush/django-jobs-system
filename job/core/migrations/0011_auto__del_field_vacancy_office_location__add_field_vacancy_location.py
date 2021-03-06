# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Vacancy.office_location'
        db.delete_column(u'core_vacancy', 'office_location')

        # Adding field 'Vacancy.location'
        db.add_column(u'core_vacancy', 'location',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=250, db_index=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Vacancy.office_location'
        raise RuntimeError("Cannot reverse this migration. 'Vacancy.office_location' and its values cannot be restored.")
        # Deleting field 'Vacancy.location'
        db.delete_column(u'core_vacancy', 'location')


    models = {
        u'core.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2', 'db_index': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'experience': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'looking_for': ('django.db.models.fields.related.ForeignKey', [], {'default': "'1'", 'to': u"orm['core.JobsCategory']"}),
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
        },
        u'core.jobscategory': {
            'Meta': {'object_name': 'JobsCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'})
        },
        u'core.vacancy': {
            'Meta': {'object_name': 'Vacancy'},
            'education': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2', 'db_index': 'True'}),
            'experience': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jobs_category': ('django.db.models.fields.related.ForeignKey', [], {'default': "'1'", 'to': u"orm['core.JobsCategory']"}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_index': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_index': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'MAN'", 'max_length': '12', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_index': 'True'})
        }
    }

    complete_apps = ['core']