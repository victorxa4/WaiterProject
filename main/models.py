from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django import forms

# fazer account para caixa?

class Account(AbstractUser):
    class Meta:
        verbose_name = 'Account'
    class account_type_choices(models.TextChoices):
        waiter = 'wt', 'waiter'
        kitchen = 'kt', 'kitchen'

    cpf = models.CharField(max_length=12, validators=[MinLengthValidator(12)])

    account_type = models.CharField(
        max_length=2,
        choices=account_type_choices.choices
    )

    def save(self):
        self.set_password(self.password)
        super(Account, self).save()

class Table(models.Model):
    class table_status_choices(models.TextChoices):
        free = 'fr', 'free'
        using = 'us', 'using'

    table_status = models.CharField(
        max_length=2,
        choices=table_status_choices.choices
    )

    number = models.AutoField(primary_key=True)


class Meal(models.Model):
    class meal_type_choices(models.TextChoices):
        pizza = 'pz', 'pizza'
        drink = 'dk', 'drink'
        snack = 'sk', 'snack'

    meal_type = models.CharField(
        max_length=2,
        choices=meal_type_choices.choices
    )

    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    
class Order(models.Model):
    closed = models.BooleanField(default=False)
    closed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    waiter = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)

class Order_Meal(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)