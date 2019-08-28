from django import forms

class LeapYearForm(forms.Form):
    year = forms.IntegerField(
        label='',
        # Substituí "TextInput" por "NumberInput"
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Descubra se um ano é bissexto',
                'aria-label': 'LeapYear',
                'aria-describedby': 'add-btn',
            }
        )
    )

