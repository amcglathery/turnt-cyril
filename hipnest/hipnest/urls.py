from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'suggest.views.index'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root' : settings.STATIC_ROOT}),

    # Examples:
    #  url(r'^$', 'hipnest.views.index', name='index'),
    # url(r'^hipnest/', include('hipnest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
