from django.urls import include, path

from . import views

urlpatterns = [
    path('api/product/', views.ProductListCreate.as_view()),
]