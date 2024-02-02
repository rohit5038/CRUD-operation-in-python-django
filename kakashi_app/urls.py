from django.urls import path
from kakashi_app import views

urlpatterns = [
    path('',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('create',views.create),
    path('dashboard',views.dashboard),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
]
