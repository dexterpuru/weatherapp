from django import forms


class cityForm(forms.Form):
    city = forms.CharField(label='Enter City', max_length=100)
