from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from mailer.views import index, oauth

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gabda.views.home', name='home'),
    # url(r'^gabda/', include('gabda.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^oauth/', oauth),
)
