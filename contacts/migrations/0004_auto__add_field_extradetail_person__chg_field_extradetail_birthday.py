# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ExtraDetail.person'
        db.add_column('contacts_extradetail', 'person',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contacts.Person'], unique=True, null=True),
                      keep_default=False)


        # Changing field 'ExtraDetail.birthday'
        db.alter_column('contacts_extradetail', 'birthday', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):
        # Deleting field 'ExtraDetail.person'
        db.delete_column('contacts_extradetail', 'person_id')


        # Changing field 'ExtraDetail.birthday'
        db.alter_column('contacts_extradetail', 'birthday', self.gf('django.db.models.fields.DateField')())

    models = {
        'contacts.extradetail': {
            'Meta': {'object_name': 'ExtraDetail'},
            'birthday': ('django.db.models.fields.DateField', [], {'default': "''", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts.Person']", 'unique': 'True', 'null': 'True'}),
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