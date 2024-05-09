from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', "img"]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['img'].label = "Picture"
