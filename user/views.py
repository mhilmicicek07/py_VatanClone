from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import login,authenticate,logout, update_session_auth_hash
from django.contrib import messages
#! admin; admin@admin.com, pw:1234 || gokhanbyk; gokhan@gokhan.com, pw: şifre123 || kullanici; kullanici@kullanici.com, pw:şifre1234
# Create your views here.
#! LOGİN
def login_view(request):

    if request.user.is_authenticated:
        messages.info(request,'Zaten giriş yaptınız.')
        return redirect('index_page')
    
    form = UserLoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user_obj = User.objects.filter(email__iexact=email).first()

            if user_obj:
                user = authenticate(request, username=user_obj.username, password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Giriş Başarılı!')
                    return redirect('index_page')
                form.add_error(None, 'E-Mail veya şifre hatalı.')
                messages.error(request, 'E-Mail veya şifre hatalı.')
            else:
                form.add_error('email', 'Bu E-Mail Mevcut Değil!')
        else:
            messages.warning(request,'Bilgilerinizi Gözden Geçirin!')

    return render(request, 'user/login.html', {
        'form': form,
    })
#! LOGİN
   
#? REGİSTER
def register_view(request):

    if request.user.is_authenticated:

        return redirect('index_page')

    form = Register(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username = username, password = password)
            login(request,user)
            messages.info(request,'Aramıza Hoşgeldiniz! :)')
            return redirect('index_page')
        messages.warning(request, 'Lütfen formunuzu gözden geçirin.')

    return render(request, 'user/register.html', {
        'form':form,
    })
#? REGİSTER

#* CHANGE-PASSWORD
@login_required
def change_password_view(request):

    if request.method == 'POST':
        form = ChangePassword(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz Başarıyla Değiştirildi!')
            return redirect('index_page')
        else:
            messages.warning(request, 'Lütfen doğru bilgileri girin.')
            return render(request, 'user/change-password.html', {
                'form': form,
            })

    form = ChangePassword(request.user)
    return render(request, 'user/change-password.html', {
        'form': form,
    })
#* CHANGE-PASSWORD

#* LOGOUT
def logout_view(request):
    logout(request)
    messages.error(request,'Çıkış yapıldı, Yine Bekleriz!')
    return redirect('index_page')
#* LOGOUT
