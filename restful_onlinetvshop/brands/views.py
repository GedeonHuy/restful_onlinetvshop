from rest_framework import generics

from .models import Brand
from .serializers import BrandSerializer


class BrandListCreate(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetail(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandUpdate(generics.UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDelete(generics.DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer