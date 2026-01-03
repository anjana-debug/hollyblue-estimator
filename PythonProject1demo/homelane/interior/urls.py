from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('step2/', views.step2, name='step2'),
]
