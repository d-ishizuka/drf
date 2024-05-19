from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(
          label='name', \
          widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    mail = forms.CharField(
          label='mail', \
          widget=forms.EmailInput(attrs={'class': 'form-control'})
        )
    age = forms.IntegerField(
          label='age', \
          widget=forms.NumberInput(attrs={'class': 'form-control'})
        )

class SessionForm(forms.Form):
    session = forms.CharField(label="session", required=False, \
                              widget=forms.TextInput(attrs={'class': 'form-control'}))