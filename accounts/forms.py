from django import forms
from accounts.models import User, Profile
from phonenumber_field.formfields import PhoneNumberField 


class ProfileForm(forms.ModelForm):
    
    phone = PhoneNumberField()
    full_name = forms.CharField(max_length=50)
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['phone'].initial = user.phone
            self.fields['full_name'].initial = user.full_name
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs.update({'class':'form-input'})
            # self.fields[field].widget.attrs.update({'style': 'width: 350px;'})
        # Set email field as read-only

    class Meta:
        model = Profile
        fields = ['phone','full_name','bio','profile_picture']