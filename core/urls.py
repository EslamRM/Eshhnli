from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('how_work/',views.how_work,name = 'how-work'),
    path('offer/',views.offers,name = 'offers'),
    path('orders/',views.orders,name = 'orders'),
    path('order/', views.order, name='order'),
    path('support/',views.support,name = 'support'),
    path('cart/', views.cart, name='cart'),
    path('get/',views.api,name='api'),
    path('add_to_cart/',views.add_cart,name='add_cart'),
    path('clear_cart/',views.clear_cart,name='clear_cart'),
    path('delete_itm/<int:id>/',views.clear_item,name='delete_itm'),
    path('edit_itm/<int:id>/',views.edit_item,name='edit_itm'),
]