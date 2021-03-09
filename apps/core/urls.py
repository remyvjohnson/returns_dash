from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('return-reasons/', views.bar_chart, name='return-reasons'),
    path('top-return-styles/', views.highest_returned_styles, name='top-return-styles'),
    path('about/', views.about, name='about'),
]
