from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='list view'),
    path('new_list/', views.new_list, name='new list'),
    path('delete_list/<int:list_id>/', views.delete_list, name='delete list'),
    path('<int:list_id>/new_item', views.new_item, name='new item'),
    path('<int:list_id>/delete_item/<int:item_idx>', views.delete_item, name='delete item'),
]
