from django import forms
from .models import *


class PapaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PapaForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            if not isinstance(field.field, forms.BooleanField):
                field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Parce
        exclude = ("user",)
