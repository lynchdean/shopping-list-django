from django import forms


class NewListForm(forms.Form):
    name = forms.CharField(label='name', max_length=60)
