from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import widgets

#! LOGİN
class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'E-Mail Giriniz:'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Şifre Giriniz:'}))

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email = email).exists():
            self.add_error('email', 'Bu E-Mail Mevcut Değil!')

        return email
#! LOGİN

#? REGİSTER
# class FullNameField(forms.CharField):
#     def to_python(self, value):
#         value = ' '.join(value.split())  # Boşlukları temizler
#         return value

class Register(UserCreationForm):
    # phone = forms.CharField(max_length=15)
    # full_name = FullNameField(max_length=60)
    # GENDER_CHOICES = (
    #     ('E', 'Erkek'),
    #     ('K', 'Kadın'),
    #     ('D', 'Diğer'),
    # )
    # gender = forms.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model = User
        fields = ('username','email','password1','password2',) #'phone','gender'

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username','email','password1','password2']: #'phone','gender',
            self.fields[fieldname].help_text = None

        # self.fields['full_name'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'Adınız Soyadınız'})
        self.fields['username'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'Kullanıcı Adınız'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class':'form-control','placeholder':'Email Adresiniz'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class':'form-control','placeholder':'Şifreniz'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class':'form-control','placeholder':'Şifreniz Tekrar'})
        # self.fields['phone'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'Telefon Numaranız'})
#? REGİSTER

#* CHANGE-PASSWORD
class ChangePassword(PasswordChangeForm):
    # class Meta:
    #     model = User
    #     fields = ('old_password', 'new_password1', 'new_password2')
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class':'form-control','placeholder':'Eski Şifreniz'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class':'form-control','placeholder':'Yeni Şifreniz'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class':'form-control','placeholder':'Yeni Şifreniz Tekrar'})
#* CHANGE-PASSWORD