from django.urls import include, path

from . import views

urlpatterns = [
    #test-start
    path('product/<str:pk>/', views.Detail.as_view()),
    #test-end

    path('api/product/', views.ProductListCreate.as_view()),
    path('api/product/<int:pk>/', views.ProductDetail.as_view()),
    path('api/product/<int:pk>/update/', views.ProductUpdate.as_view()),
    path('api/product/<int:pk>/delete/', views.ProductDelete.as_view()),
]