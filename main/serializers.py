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

def set_waiter(self,request):
    request.data.waiter = request.user

class Order_Meal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Meal
        fields = '__all__'

class Order_Serializer(serializers.ModelSerializer):
    order_meals = Order_Meal_Serializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['closed', 'closed_at', 'created_at', 'table', 'waiter', 'order_meals']
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
        
        if value:
            if instance.table.table_status == 'us':
                instance.table.table_status = 'fr'
                instance.table.save()
        else:
            if instance.table.table_status == 'fr':
                instance.table.table_status = 'us'
                instance.table.save()
            
        return value
        
class Meal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'