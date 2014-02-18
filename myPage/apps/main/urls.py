from django.conf.urls import patterns, url
from myPage.apps.main.views import ClientsView

urlpatterns = patterns('myPage.apps.main.views',
                       url(r'^$', 'index_view', name='url_index'),
                       url(r'clients/$', ClientsView.as_view(), name='clients'),
)