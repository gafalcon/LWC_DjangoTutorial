from django import forms
from .models import Join

class EmailForm(forms.Form):
    """
    Displays a form with an email field
    """
    email = forms.EmailField()

class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ['email']
