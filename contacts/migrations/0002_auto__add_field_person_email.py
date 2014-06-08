# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.email'
        db.add_column('contacts_person', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.email'
        db.delete_column('contacts_person', 'email')


    models = {
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