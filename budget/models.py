from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    (0, "INCOME"),
    (1, "EXPENSES")
)

class Account(models.Model):
    name = models.CharField(unique=True, null=False, max_length=32)
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Client(models.Model):
#     username = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.username

class Transaction(models.Model):
    account = models.ForeignKey(Account, null=False, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateField()
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)



