from rest_framework import serializers
from budget.models import Account, Transaction, CATEGORY_CHOICES


class AccountSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=32)
    category = serializers.ChoiceField(choices=CATEGORY_CHOICES)
    description = serializers.CharField(max_length=100)
    class Meta:
        model = Account
        fields = ['name', 'category', 'description']


    # def create(self, validated_data):
    #     return Konto(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('email', instance.name)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.description = validated_data.get('description', instance.description)
    #     return instance


class TransactionSerializer(serializers.ModelSerializer):
    name = serializers.models.CharField(max_length=32)
    amount = serializers.IntegerField()
    date = serializers.DateField
    class Meta:
        model = Transaction
        fields = ['account', 'amount', 'date']

    # def create(self, validated_data):
    #     return Transaction(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.amount = validated_data.get('amount', instance.amount)
    #     instance.date = validated_data.get('date', instance.date)
    #     return instance