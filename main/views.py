from .permissions import *
from .serializers import *
from rest_framework import generics

class Table_View(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = Table_Serializer
    permission_classes = [Waiter_ReadOnly]
class Table_RetrieveUpdateDestroy_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    permission_classes = [Waiter_ReadOnly]
    serializer_class = Table_Serializer

class Order_View(generics.ListCreateAPIView):
    queryset = Order.objects.filter()
    permission_classes = [Waiter_FullAccess|Kitchen_ReadOnly]
    serializer_class = Order_Serializer
class Order_RetrieveUpdateDestroy_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = [Waiter_FullAccess|Kitchen_ReadOnly]
    serializer_class = Order_Single_Serializer

class Meal_View(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    permission_classes = [ReadOnly]
    serializer_class = Meal_Serializer
class Meal_RetrieveUpdateDestroy_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    permission_classes = [ReadOnly]
    serializer_class = Meal_Serializer

class Order_Meal_View(generics.ListCreateAPIView):
    queryset = Order_Meal.objects.all()
    permission_classes = [Waiter_FullAccess|Kitchen_ReadOnly]
    serializer_class = Order_Meal_Serializer
class Order_Meal_RetrieveUpdateDestroy_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order_Meal.objects.all()
    permission_classes = [Waiter_FullAccess|Kitchen_ReadOnly]
    serializer_class = Order_Meal_Single_Serializer