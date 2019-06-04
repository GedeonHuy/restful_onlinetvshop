from rest_framework import generics

from .models import Order, OrderItem
from .models import CustomUser as User
from .serializers import OrderCreateSerializer, OrderSerializer, UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    lookup_url_kwarg = {
        'pk': None,
        'owner_id': None
    }

class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdate(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDelete(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserOrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = {
        'pk': None,
        'owner_id': None
    }