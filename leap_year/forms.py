from django import forms

class LeapYearForm(forms.Form):
    year = forms.IntegerField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Descubra se um ano é bissexto',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn',
            }
        )
    )