from django.urls import path
from . import views

urlpatterns = [
    path('create/<str:title>/',views.Create,name='Create'),
    path('list/',views.List,name='List'),
    path('edit/<int:id>/<str:new>/',views.Edit,name='Edit'),
    path('check/<int:id>/',views.Check,name='Check'),
    path('back/<int:id>/',views.Back,name='Back'),
    path('delete/<int:id>/',views.Delete,name='Delete'),
]