from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.post_list, name='post_list'), #so only an empty string will match. Because in Django URL resolvers, 'http://127.0.0.1:8000/' is not a part of the URL.
]