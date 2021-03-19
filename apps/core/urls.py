from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('return-rate-by-category/', views.cat_rr, name='return-rate-by-category'),
    path('return-reasons/', views.return_reasons, name='return-reasons'),
    path('top-return-styles/', views.highest_returned_styles, name='top-return-styles'),
]
