from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Product
        fields = ['name',
                  'quantity',
                  'category',
                  'price'
                  ]

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get("name")
            description = cleaned_data.get("description")

            if name == description:
                raise ValidationError(
                    "Описание не должно быть идентичным названию товара."
                )
            return cleaned_data