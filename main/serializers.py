from rest_framework import serializers
from .models import *
from .permissions import *

class Account_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
        write_only = ['password']

class Table_Serializer(serializers.ModelSerializer):
    permission_classes = [ReadOnly]
    class Meta:
        model = Table
        fields = '__all__'

class Order_Meal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Meal
        fields = '__all__'

class Order_Meal_ToOrder_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Meal
        fields = ['meal']
class Order_Serializer(serializers.ModelSerializer):
    order_meals = Order_Meal_ToOrder_Serializer(many=True, required=True)

    class Meta:
        model = Order
        fields = ['pk', 'closed', 'closed_at', 'created_at', 'table', 'waiter', 'order_meals']
        extra_kwargs = {'waiter': {'default': serializers.CurrentUserDefault()}}

    def validate_table(self, value):
        if value.table_status == 'fr':
            return value
        else:
            raise serializers.ValidationError('Table already being used.')
    
    def create(self, validated_data):
        print(validated_data)
        table = validated_data['table']
        if table.table_status == 'fr':
            table.table_status = 'us'
            table.save()
        
        try:
            if validated_data['closed']:
                if table.table_status == 'us':
                    table.table_status = 'fr'
                    table.save()
            else:
                if table.table_status == 'fr':
                    table.table_status = 'us'
                    table.save()
        except:
            table.table_status = 'us'
            table.save()

        order_meals_data = validated_data.pop('order_meals')
        print(validated_data)
        order_instance = Order.objects.create(**validated_data)

        for order_meal in order_meals_data:
           Order_Meal.objects.create(order=order_instance, meal=order_meal['meal'])

        return order_instance
class Order_Serializer_Single_Serializer(serializers.ModelSerializer):
    table = Table_Serializer(required=False)
    class Meta:
        model = Order
        fields = ['closed', 'closed_at', 'created_at', 'table', 'waiter']
        extra_kwargs = {'waiter': {'default': serializers.CurrentUserDefault()}}

    def validate_table(self, value):
        if value.table_status == 'fr':
            value.table_status = 'us'
            value.save()
            return value
        else:
            raise serializers.ValidationError('Table already being used.')
        
    def validate_closed(self, value):
        instance = getattr(self, 'instance', None)
        table = instance.table
        if value:
            if table.table_status == 'us':
                table.table_status = 'fr'
                print(table.table_status)
                table.save(update_fields=['table_status'])
        else:
            if table.table_status == 'fr':
                table.table_status = 'us'
                table.save(update_fields=['table_status'])
            
        return value
        
class Meal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'