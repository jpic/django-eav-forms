# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Form'
        db.create_table('eav_forms_form', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contenttype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
        ))
        db.send_create_signal('eav_forms', ['Form'])

        # Adding model 'Tab'
        db.create_table('eav_forms_tab', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eav_forms.Form'])),
        ))
        db.send_create_signal('eav_forms', ['Tab'])

        # Adding model 'Field'
        db.create_table('eav_forms_field', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model_field_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tab', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eav_forms.Tab'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('help_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('eav_forms', ['Field'])


    def backwards(self, orm):
        # Deleting model 'Form'
        db.delete_table('eav_forms_form')

        # Deleting model 'Tab'
        db.delete_table('eav_forms_tab')

        # Deleting model 'Field'
        db.delete_table('eav_forms_field')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eav_forms.field': {
            'Meta': {'object_name': 'Field'},
            'help_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_field_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'tab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eav_forms.Tab']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'eav_forms.form': {
            'Meta': {'object_name': 'Form'},
            'contenttype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eav_forms.tab': {
            'Meta': {'object_name': 'Tab'},
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eav_forms.Form']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['eav_forms']