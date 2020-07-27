from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    confirm_email=forms.EmailField()
    contact=forms.RegexField(regex="^[6-9]\d{9}", required=False)
    address1=forms.CharField()
    address2=forms.CharField(required=False)
    postal_code=forms.RegexField(regex="^[6-9]\d{6}")
    is_seller=forms.BooleanField()
    class Meta:
        model = get_user_model()
        fields=('first_name','last_name','username','email','confirm_email','contact','is_seller','password1','password2','address1','address2','postal_code')

    def clean(self):
        cleaned_data=super().clean()
        if cleaned_data.get('email') != cleaned_data.get('confirm_email'):
            raise forms.ValidationError('Your Email and Confirm Email is not match',code='Invalid')


class UserUpdateForm(forms.ModelForm):
    address2=forms.CharField(required=False)
    class Meta:
        model = get_user_model()
        fields=('first_name','last_name','username','email','contact','address1','address2','postal_code')
