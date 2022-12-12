from django.urls import path

from . import views

urlpatterns = [
    path('entyti/', views.Entyti_view.as_view(), name='entyti'),
]
