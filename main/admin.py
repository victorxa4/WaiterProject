from django.contrib import admin
from .models import Account, Table, Meal, Order, Order_Meal

admin.site.register(Account)
admin.site.register(Table)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(Order_Meal)