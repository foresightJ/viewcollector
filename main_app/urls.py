from django.urls import path
from . import views
# from .views import ViewListView

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # path('views/', views.views_index, name='index'),---initial Function View
  path('views/', views.ViewListView.as_view(), name='views_index'),
  path('views/<int:view_id>/', views.views_detail, name='detail'),
  path('views/create/', views.ViewCreate.as_view(), name='views_create'),
  path('views/<int:pk>/update/', views.ViewUpdate.as_view(), name='views_update'),
  path('views/<int:pk>/delete/', views.ViewDelete.as_view(), name='views_delete'),
  path('views/<int:view_id>/add_event/', views.add_event, name='add_event'),
  
  # associate a toy with a cat (M:M)
  path('views/<int:view_id>/assoc_star/<int:star_id>/', views.assoc_star, name='assoc_star'),
  
  # unassociate a toy and cat
  path('views/<int:view_id>/unassoc_star/<int:star_id>/', views.unassoc_star, name='unassoc_star'),
  path('stars/', views.StarList.as_view(), name='stars_index'),
  path('stars/<int:pk>/', views.StarDetail.as_view(), name='stars_detail'),
  path('stars/create/', views.StarCreate.as_view(), name='stars_create'),
  path('stars/<int:pk>/update/', views.StarUpdate.as_view(), name='stars_update'),
  path('stars/<int:pk>/delete/', views.StarDelete.as_view(), name='stars_delete'),
]