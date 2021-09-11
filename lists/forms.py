from django import forms


class NewListForm(forms.Form):
    name = forms.CharField(label='name', min_length=1, max_length=60)
