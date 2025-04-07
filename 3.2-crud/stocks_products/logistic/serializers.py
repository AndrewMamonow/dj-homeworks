from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']


    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)
        # создаем продукт по его параметрам
        for position in positions:
            StockProduct.objects.create(
                stock = stock,
                product = position['product'],
                quantity = position['quantity'],
                price=position['price']
            )

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        # обновляем продукт по его параметрам
        for position in positions:
            object = StockProduct.objects.filter(
                stock = stock, product = position['product'])

            object.update_or_create(
                stock = stock,
                product = position['product'],
                defaults={
                    'quantity': position['quantity'],
                    'price': position['price']
                }
            )

        return stock
