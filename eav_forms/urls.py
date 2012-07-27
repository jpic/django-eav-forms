from django.conf.urls.defaults import patterns, url

import views

urlpatterns = patterns('',
    url(r'create/$', views.FormCreateView.as_view(),
        name='eav_forms_form_create'),
    url(r'update/(?P<pk>\d+)/$', views.FormUpdateView.as_view(),
        name='eav_forms_form_update'),
)
