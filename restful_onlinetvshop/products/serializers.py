from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = ('title', 'price', 'quantity', 'description', 'image_url', 'brand')