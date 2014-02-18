from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myPage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^main/admin/', include(admin.site.urls)),
    url(r'^main/', include('myPage.apps.main.urls')),
)
