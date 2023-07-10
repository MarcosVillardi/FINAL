from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from . import views

urlpatterns = [
    path('reserva_list/', views.Reserva_list.as_view(), name='reserva_list'),
    path('reserva_create/',staff_member_required( views.Reserva_create.as_view()), name='reserva_create'),
    path('reserva_delete/<int:pk>',staff_member_required( views.Reserva_delete.as_view()), name='reserva_delete'),
    path('reserva_update/<int:pk>', staff_member_required(views.Reserva_update.as_view()), name='reserva_update'),
    path('reserva_index', views.reserva_index, name='reserva_index'),
    path('garaje_list/', views.Garaje_list.as_view(), name='garaje_list'),
    path('garaje_create/', staff_member_required(views.Garaje_create.as_view()), name='garaje_create'),
    path('garaje_delete/<int:pk>', staff_member_required(views.Garaje_delete.as_view()), name='garaje_delete'),
    path('garaje_update/<int:pk>', staff_member_required(views.Garaje_update.as_view()), name='garaje_update'),
    path('garaje_index', views.garaje_index, name='garaje_index'),

]
urlpatterns += staticfiles_urlpatterns()