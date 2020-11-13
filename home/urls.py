

from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index_view,name='index_all'),
    path('<str:parent_or_child>/<int:pk>',views.index_view,name='index'),

]