


from django.urls import path,include
from . import views
from .views import Login,Register,Index,Cart,CheckOut,Search,OrderView,Detail
from .views import logout
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(),name='index_all'),
    path('<str:parent_or_child>/<int:pk>',Index.as_view(),name='index'),
    path('login',Login.as_view(),name='login'),
    path('register',Register.as_view(),name='register'),
    path('logout',logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('check-out',CheckOut.as_view(),name='checkout'),
    path('search',Search.as_view(),name='search'),
    path('orders',auth_middleware(OrderView.as_view()), name='orders'),
    path('product_detail/<slug:slug>/',Detail.as_view(),name='detail'),
]
