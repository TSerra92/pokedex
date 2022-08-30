from socket import fromshare

from django import forms


class PokeForm(forms.Form):
    pokemon = forms.CharField(label='Pokemon: ', max_length=100)
