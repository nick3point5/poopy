from django import forms
from .models import Poop, Food


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

class FoodForm(forms.ModelForm):
    
    class Meta:
        model = Food
        fields = [
            'name',
            'note',
            ]
        labels = {
            'name':'Name',
            'note':'Notes',
        }
