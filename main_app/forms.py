from django import forms
from .models import Bristol_Type, Color, Poop


class PoopForm(forms.ModelForm):

    class Meta:
        model = Poop
        fields = [
            'type',
            'note',
            'color',
            ]
        labels = {
            'type':'Bristol Type',
            'note':'Notes',
            'color':'Color'
        }

    def __init__(self, *args, **kwargs):
        super(PoopForm,self).__init__(*args, **kwargs)
        self.fields['color'].empty_label = "Select"
        self.fields['type'].empty_label = "Select"

