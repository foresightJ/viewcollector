from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('views/', views.views_index, name='about'),
  path('views/<int:view_id>/', views.views_detail, name='detail')
]