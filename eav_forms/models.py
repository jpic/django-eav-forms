from django.db import models
from django.utils.translation import ugettext_lazy as _

KIND_CHOICES = (
    ('int', _('integer')),
    ('float', _('decimal number')),
    ('char', _('short text')),
    ('text', _('text')),
    ('datetime', _('date and time')),
    ('date', _('date only')),
    ('time', _('time only')),
    ('image', _('image')),
    ('file', _('file')),
)


class Form(models.Model):
    name = models.CharField(max_length=100)
    contenttype = models.ForeignKey('contenttypes.ContentType')

    def __unicode__(self):
        return u'%s / %s' % (self.contenttype.model, self.name)


class Tab(models.Model):
    name = models.CharField(max_length=100)
    form = models.ForeignKey('Form')

    def __unicode__(self):
        return u'%s / %s' % (self.name, self.form)


class Field(models.Model):
    name = models.CharField(max_length=100)
    model_field_name = models.CharField(max_length=100)
    tab = models.ForeignKey('Tab')
    type = models.CharField(max_length=12, choices=KIND_CHOICES)
    order = models.IntegerField()

    help_text = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'%s / %s' % (self.name, self.tab)
