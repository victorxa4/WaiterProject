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

class Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # exclude = ['waiter']
        fields = '__all__'
        #read_only_fields = ['waiter']
        extra_kwargs = {'waiter': {'default': serializers.CurrentUserDefault()}}