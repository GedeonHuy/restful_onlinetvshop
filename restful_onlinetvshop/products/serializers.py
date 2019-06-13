from rest_framework import serializers

from .models import Product
from brands.models import Brand
from brands.serializers import BrandSerializer


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'quantity', 'description', 'image_url', 'brand')