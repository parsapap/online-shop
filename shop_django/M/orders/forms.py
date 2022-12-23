from django import forms


class CardAddForm(forms.Form):
    quantity = forms.IntegerField(label='', min_value=1, max_value=9,
                                  widget=forms.NumberInput(
                                      attrs={'class': 'form-control w-25', 'placeholder': 'Quantity'}))
