'''
Created on 25-Jan-2020

@author: Sarath Sankar
'''

from django import forms
from django.core import validators

alphanumeric = validators.RegexValidator(r'^[0-9_a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
alphaspecial = validators.RegexValidator(r'^[a-zA-Z+-]*$', 'Only characters along with " + - " are allowed.')
characters_only = validators.RegexValidator(r'^[a-zA-Z_]*$', 'Only characters are allowed.')
character_special = validators.RegexValidator(r"^[' .a-z_A-Z_0-9]*$", 'Please enter a valid character.')
decimal_only = validators.RegexValidator(r"^[0-9]+\.?[0-9]+$", 'Please enter a valid decimal.')

class AdminLoginForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', 
                                widget=forms.TextInput(attrs=dict(required=True,
                                                                max_length=30, 
                                                                placeholder='Username')), 
                                label=("Username"), 
                                error_messages={ 'invalid': ("Username must contain only letters, numbers and underscores") },
                                validators=[alphanumeric]
                                )
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(
                                                                    required=True, 
                                                                    max_length=30, 
                                                                    render_value=False, 
                                                                    placeholder='Password'),
                                                          ),
                                                          label=("Password"))
    
    def __init__(self, *args, **kwargs):
        super(AdminLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-control form-control-line"
        self.fields['password'].widget.attrs['class'] = "form-control form-control-line"














