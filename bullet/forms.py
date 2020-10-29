from django.forms import ModelForm
from bullet.models import Customer


class CustomerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = "Your name"
        self.fields['phonenumber'].widget.attrs['placeholder'] = "Your phonenumber"
        self.fields['email'].widget.attrs['placeholder'] = "Your email"
        self.fields['message'].widget.attrs['placeholder'] = "Please, write your message"
        self.fields['name'].label = ''
        self.fields['phonenumber'].label = ''
        self.fields['email'].label = ''
        self.fields['message'].label = ''

    class Meta:
        model = Customer
        fields = ["name", "phonenumber", "email", "message"]
