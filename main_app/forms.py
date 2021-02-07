from django import forms
from .models import Poop


class PoopForm(forms.ModelForm):

    class Meta:
        model = Poop
        fields = [
            'Bristol_Type',
            'note',
            'color',
            ]
        labels = {
            'Bristol_Type':'Type',
            'note':'Notes',
        }

    def __init__(self, *args, **kwargs):
        super(PoopForm,self).__init__(*args, **kwargs)
        self.fields['color'].empty_label = "Select"

