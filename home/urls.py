


from django.urls import path,include
from . import views
#from .views import index,register
from  .views import Login,Register,Index,Cart
from .views import logout
urlpatterns = [
    path('', Index.as_view(),name='index_all'),
    path('<str:parent_or_child>/<int:pk>',Index.as_view(),name='index'),
    path('login',Login.as_view(),name='login'),
    path('register',Register.as_view(),name='register'),
    path('logout',logout,name='logout'),
    path('cart',Cart.as_view(),name='cart')
]
