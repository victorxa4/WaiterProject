from rest_framework import permissions
from .permissions import *
from .serializers import *
from rest_framework import generics

# https://www.django-rest-framework.org/api-guide/generic-views/

class Table_View(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = Table_Serializer

class Order_View(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    permission_classes = [Waiter_FullAccess|Kitchen_ReadOnly]
    serializer_class = Order_Serializer
class Order_Destroy_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    permission_classes = [Waiter_FullAccess]
    serializer_class = Order_Serializer