from django.contrib import admin
from django.urls import path,include
from . import views
from accounts import views as accounts_views


urlpatterns = [
    path('',views.index,name='home'),
    path('product/',views.products,name='product'),
    path('support/',views.support,name='support'),
    path('Tracker/',views.Tracker,name='Tracker'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove-from-cart_/<int:product_id>/', views.remove_from_cart_view, name='remove_from_cart_view'),
    path('cart/update/<int:product_id>/<str:action>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('skiping',views.skiping,name='skiping'),
    path('checkout',views.checkout,name='checkout'),
    path('placeorder',views.placeorder,name='placeorder'),
    path('track_order/', views.track_order, name='track_order'),

]


