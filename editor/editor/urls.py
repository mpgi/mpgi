from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.editor, name='editor'),
    url(r'^create/project/$', views.create_project, name='create_project'),
    url(r'^load_project/$', views.load_project, name='load_project'),
]
