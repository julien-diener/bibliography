from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home', name='home'),
    
    url(r'^user/', 'views.publication', name='publication'),

    url(r'^admin/', include(admin.site.urls)),
)
