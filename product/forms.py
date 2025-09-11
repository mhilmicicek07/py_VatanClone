from django import forms
from .models import Urun

class UrunEkle(forms.ModelForm):
    class Meta:
        model = Urun
        fields = ["urun_name", "urun_description", "urun_price", "urun_image", "urun_category"]
        widgets = {
            "urun_description": forms.Textarea(attrs={"rows": 3}),
        }

    def clean_urun_price(self):
        price = self.cleaned_data.get("urun_price")
        if price is not None and price <= 0:
            raise forms.ValidationError("Fiyat 0'dan büyük olmalı!")
        return price