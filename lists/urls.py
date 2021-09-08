from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_list/', views.new_list, name='new list'),
    path('<int:list_id>/', views.list_view, name='list view'),
    path('delete_list/<int:list_id>/', views.delete_list, name='delete list'),
]
