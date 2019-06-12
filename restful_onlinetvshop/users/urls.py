from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    # user site
    path('api/user/', views.UserListCreate.as_view()),
    path('api/user/<str:pk>/', views.UserDetail.as_view()),
    path('api/user/<str:pk>/update/', views.UserUpdate.as_view()),
    path('api/user/<str:pk>/delete/', views.UserDelete.as_view()),

    # order site
    path('api/order/', views.OrderListCreate.as_view()),
    path('api/order/<str:pk>/', views.OrderDetail.as_view()),
    path('api/order/<str:pk>/update/', views.OrderUpdate.as_view()),
    path('api/order/<str:pk>/delete/', views.OrderDelete.as_view()),
    path('api/order/<str:pk>/<int:owner_id>/', views.UserOrderDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)