


from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index.as_view(),name='index_all'),
    
    path('<str:parent_or_child>/<int:pk>',views.index.as_view(),name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register')

]
