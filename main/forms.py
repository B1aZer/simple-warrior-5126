from django.forms import ModelForm
from models import SSL
from django import forms
import re


class SSLForm(ModelForm):
    class Meta:
        model = SSL
    def clean_phone(self):
        value = self.cleaned_data.get('phone',None)
        if value:
            phonePattern = re.compile(r'''
                    # don't match beginning of string, number can start anywhere
            (\d{3})     # area code is 3 digits (e.g. '800')
            \D*         # optional separator is any number of non-digits
            (\d{3})     # trunk is 3 digits (e.g. '555')
            \D*         # optional separator
            (\d{4})     # rest of number is 4 digits (e.g. '1212')
            \D*         # optional separator
            (\d*)       # extension is optional and can be any number of digits
            $           # end of string
            ''', re.VERBOSE)
            if phonePattern.search(value):
                return value
            else:
                raise forms.ValidationError('%s is not a valid phone number' % value)

