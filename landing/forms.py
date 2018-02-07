from django import forms
from .models import *


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = [""]

class ToysFilterForm(forms.Form):
    min_price = forms.DecimalField(label="от", required=False)
    max_price = forms.DecimalField(label="до", required=False)
    ordering = forms.ChoiceField(label="сортировка", required=False, choices=[
        ["price", "от дешевых к дорогим"],
        ["-price", "от дорогих к дешевым"]
    ])
