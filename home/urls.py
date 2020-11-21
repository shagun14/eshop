


from django.urls import path,include
from . import views
from  .views import Login,Register,Index,Cart,CheckOut,Search
from .views import logout
urlpatterns = [
    path('', Index.as_view(),name='index_all'),
    path('<str:parent_or_child>/<int:pk>',Index.as_view(),name='index'),
    path('login',Login.as_view(),name='login'),
    path('register',Register.as_view(),name='register'),
    path('logout',logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('check-out',CheckOut.as_view(),name='checkout'),
    path('search',Search.as_view(),name='search'),
]
