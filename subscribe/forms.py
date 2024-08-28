
from django import forms

from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields ='__all__'
        labels ={
            'first_name':_("Enter First Name:")
        }
        error_messages={
            'first_name':{
                'required':_('Please Enter First Name')
            },
            'last_name':{
                'required':_('Please Enter Last Name')
            },
            'email':{
                'required':_('Please Enter Email')
            }
        }

# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError('Invalid Last Name')
#     return value
# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=200)
#     last_name = forms.CharField(max_length=200, validators=[validate_comma])
#     email = forms.EmailField(max_length=200)

    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if "," in data:
    #         raise forms.ValidationError("Invalid First Name")
    #     return