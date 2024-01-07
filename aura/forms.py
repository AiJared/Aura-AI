from aura.models import Meeting
from django import forms

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['pychiatrist']

    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs.update({'class':'form-control'})