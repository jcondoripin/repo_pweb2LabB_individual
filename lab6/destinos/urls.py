from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('show/<id>', views.show, name='show'),
    path('edit', views.edit, name='edit'),
]