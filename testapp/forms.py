from django import forms
from testapp.models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register

        fields = '__all__'
        labels = {
            'first_name' :'First Name',
            'dob':'Date of birth',
            'email':'Email',
            'mobilenumber':'Mobile Number'
            }
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control form-control-solid',}),
            'dob' : forms.DateInput(attrs={'class':'datepicker form-control required',}),
            'email' : forms.TextInput(attrs={'class': 'form-control form-control-solid',}),
            'mobilenumber' : forms.TextInput(attrs={'class': 'form-control form-control-solid', }),
        }
