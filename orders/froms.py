from django import forms


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=9)


class DiscountApplyForm(forms.Form):
    code = forms.CharField()
