from django import forms

from budget.models import Account, Transaction


class ModelAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

class ModelTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"