from django.urls import path
from . import views
from .views import Addpdtview, Viewpdtview, Uppdtview, Delpdtview, Usersview, Restview, Userpdtview, Userpdtdetview, \
    Buy, success, Value, Buy1

urlpatterns = [
    path('', views.index, name='index'),
    path('orderplaced/', views.orderplaced),
    path('restaurant/', views.restuarent, name='restuarant'),
    path('register/user/', views.customerRegister, name='register'),
    path('login/user/', views.customerLogin, name='login'),
    path('login/restaurant/', views.restLogin, name='rlogin'),
    path('register/restaurant/', views.restRegister, name='rregister'),
    path('profile/restaurant/', views.restaurantProfile, name='rprofile'),
    path('profile/user/', views.customerProfile, name='profile'),
    path('user/create/', views.createCustomer, name='ccreate'),
    path('user/update/<int:id>/', views.updateCustomer, name='cupdate'),
    path('restaurant/create/', views.createRestaurant, name='rcreate'),
    path('restaurant/update/<int:id>/', views.updateRestaurant, name='rupdate'),
    path('restaurant/orderlist/', views.orderlist, name='orderlist'),
    path('restaurant/menu/', views.menuManipulation, name='mmenu'),
    path('logout/', views.Logout, name='logout'),
    path('restaurant/<int:pk>/', views.restuarantMenu, name='menu'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/admin/', views.AdminLogin, name='alogin'),
    path('profile/admin/', views.AdminProfile, name='adminprofile'),
    path('profile/viewusers/', Usersview.as_view(), name='viewusers'),
    path('profile/viewrest/', Restview.as_view(), name='viewrest'),
    path('profile/addpdt/', Addpdtview.as_view(), name='addpdt'),
    path('profile/viewpdt/', Viewpdtview.as_view(), name='viewpdt'),
    path('profile/uppdt/(?p<pk>[0-9]+)', Uppdtview.as_view(), name='uppdt'),
    path('profile/delpdt/(?p<pk>[0-9]+)', Delpdtview.as_view(), name='delpdt'),
    path('user/userpdt/', Userpdtview.as_view(), name='userpdt'),
    path('userpdtdet/(?p<pk>[0-9]+)', Userpdtdetview.as_view(), name='userpdtdet'),
    path('Buy/(?p<pk>[0-9]+)', Buy.as_view(), name='buy'),
    path('Buy/success', success, name='Buy/success'),
    path('value/', Value.as_view(), name='value'),
    path('Buy1/(?p<pk>[0-9]+)', Buy1.as_view(), name='buy1'),
    path('Buy1/success', success, name='Buy1/success'),

]
