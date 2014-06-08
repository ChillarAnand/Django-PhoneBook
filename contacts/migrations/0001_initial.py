# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('contacts_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('address', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal('contacts', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('contacts_person')


    models = {
        'contacts.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['contacts']