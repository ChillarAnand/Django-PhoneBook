# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExtraDetail'
        db.create_table('contacts_extradetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=100)),
            ('notes', self.gf('django.db.models.fields.TextField')(default='')),
            ('relationship', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('birthday', self.gf('django.db.models.fields.DateField')(default='')),
        ))
        db.send_create_signal('contacts', ['ExtraDetail'])


    def backwards(self, orm):
        # Deleting model 'ExtraDetail'
        db.delete_table('contacts_extradetail')


    models = {
        'contacts.extradetail': {
            'Meta': {'object_name': 'ExtraDetail'},
            'birthday': ('django.db.models.fields.DateField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'relationship': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100'})
        },
        'contacts.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['contacts']