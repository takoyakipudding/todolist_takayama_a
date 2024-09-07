from django.urls import path
from . import views

app_name='todos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:todo_id>/delete', views.delete, name='delete'),
    path('<int:todo_id>/update', views.update, name='update'),
    path('add/', views.add, name='add'),
    path('edit/<int:todo_id>/', views.edit, name='edit'), 
    path('signup/', views.signup, name='signup'),
    path('update_order/', views.update_order, name='update_order'),
    path('save_fcm_token/', views.save_fcm_token, name='save_fcm_token'),
]