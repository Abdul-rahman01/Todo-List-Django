from django.urls import path
from . import views

app_name = 'list'


urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
