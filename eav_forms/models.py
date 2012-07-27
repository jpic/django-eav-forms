from django.db import models
from django.utils.translation import ugettext_lazy as _

from crispy_forms.layout import Layout, Fieldset

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

    def to_crispy(self, enabled=True):
        layout = Layout()
        for tab in self.tab_set.filter(enabled=enabled):
            layout.fields.append(tab.to_crispy())
        return layout

    def enabled_tab_set(self):
        return self.tab_set.filter(enabled=True)

    def disabled_tab_set(self):
        return self.tab_set.filter(enabled=False)


def prepare_form(sender, instance, created, **kwargs):
    if not created:
        return

    model_class = instance.contenttype.model_class()
    default_tab, c = instance.tab_set.get_or_create(name='', enabled=False)

    for field in model_class._meta.fields + model_class._meta.many_to_many:
        f, c = instance.field_set.get_or_create(model_field_name=field.name,
            form=instance)

        if c:
            f.name = getattr(f, 'verbose_name', _(field.name))
            f.tab = default_tab
            f.save()

    if not instance.tab_set.filter(enabled=True).count():
        instance.tab_set.create(name='Info', enabled=True)

models.signals.post_save.connect(prepare_form, sender=Form)


class Tab(models.Model):
    name = models.CharField(max_length=100)
    form = models.ForeignKey('Form')
    order = models.IntegerField(default=0)
    enabled = models.BooleanField(default=False)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return u'%s / %s' % (self.name, self.form)

    def to_crispy(self):
        fieldset = Fieldset(self.name)
        for field in self.field_set.all():
            fieldset.fields.append(field.to_crispy())
        return fieldset


class Field(models.Model):
    name = models.CharField(max_length=100)
    model_field_name = models.CharField(max_length=100)
    help_text = models.TextField(blank=True)
    form = models.ForeignKey('Form')
    tab = models.ForeignKey('Tab', null=True, blank=True)
    kind = models.CharField(max_length=12, choices=KIND_CHOICES)
    order = models.IntegerField(default=0)

    help_text = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return u'%s / %s' % (self.name, self.tab)

    def to_crispy(self):
        return self.model_field_name
