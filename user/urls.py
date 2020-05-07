from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.base, name = 'base'),
    path('basic/', views.basic, name = 'basic'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    # path('list/', views.list, name = 'list'),
    path('<int:id>/list/', views.list, name = 'list'),
    path('assign/', views.assign, name = 'assign'),
    path('student/', views.student, name = 'student'),

   

]