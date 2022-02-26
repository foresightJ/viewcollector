from django.urls import path
from . import views
from .views import ViewListView

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # path('views/', views.views_index, name='index'),
  path('views/', ViewListView.as_view(), name='views_index'),
  path('views/<int:view_id>/', views.views_detail, name='detail')
]