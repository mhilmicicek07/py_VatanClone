from django import forms
from .models import *

class UrunEkle(forms.ModelForm):
    class Meta:
        model = Urun
        fields = ('urun_name','urun_description','urun_price','urun_image','urun_category')
        label = {
            'urun_name':'Ürün Adı',
            'urun_description':'Ürün Açıklaması',
            'urun_price':'Ürün Fiyatı',
            'urun_category':'Ürün Kategorisi',
        }

        widgets = {
            'urun_name': forms.TextInput(attrs={'class':'form-control'}),
            'urun_description': forms.TextInput(attrs={'class':'form-control'}),
            'urun_price': forms.NumberInput(attrs={'class':'form-control'}),
            # 'urun_image': forms.FileInput(attrs={'class':'form-control'}),
            # 'urun_image': forms.CharField(is_hidden=False),
            'urun_category': forms.Select(attrs={'class':'form-select'})
        }