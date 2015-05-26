from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hearts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$','users.views.login'),
    url(r'^logout/$','users.views.logout'),
    url(r'^$','users.views.home'),
    url(r'^register/$', 'users.views.register_user'),
    url(r'^admin/', include(admin.site.urls)),
)
