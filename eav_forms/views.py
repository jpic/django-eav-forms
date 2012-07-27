import copy

from django.forms.models import modelform_factory
from django.core import urlresolvers
from django.views import generic

from crispy_forms.helper import FormHelper

from models import Form, KIND_CHOICES


class FormCreateView(generic.CreateView):
    model = Form
    template_name = 'eav_forms/form_create.html'

    def get_success_url(self):
        return urlresolvers.reverse('eav_forms_form_update',
            args=(self.object.pk,))


class FormUpdateView(generic.UpdateView):
    model = Form
    template_name = 'eav_forms/form_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FormUpdateView, self).get_context_data(*args,
            **kwargs)

        model = self.object.contenttype.model_class()

        context['KIND_CHOICES'] = KIND_CHOICES

        return context