from django import forms
from .helpers.statics import months


class InputDateForm(forms.Form):
    months_keys = list(months.items())
    selected_months = forms.MultipleChoiceField(
        choices=months_keys,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
