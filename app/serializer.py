from rest_framework import serializers
from app.models import Product


class ReactProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category',
                  'price',
                  'in_Stocked',
                  'image',
                  'ingredients']
