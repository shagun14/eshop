

from django.urls import path,include
from . import views
from home.views import login
urlpatterns = [
    path('',views.index_view,name='index_all'),
    path('<str:parent_or_child>/<int:pk>',views.index_view,name='index'),
    path('login',views.login,name='login')

]
