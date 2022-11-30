from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('newform', views.newform, name='newform'),
    path('form', views.form, name='form'),


    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

]

