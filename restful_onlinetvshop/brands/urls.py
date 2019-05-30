from django.urls import include, path

from . import views

urlpatterns = [
    path('api/brand/', views.BrandListCreate.as_view()),
]
