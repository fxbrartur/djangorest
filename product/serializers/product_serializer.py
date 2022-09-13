from rest_framework import serializers

from product.models.product import Category, Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True)

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "active",
            "category",
        ]
