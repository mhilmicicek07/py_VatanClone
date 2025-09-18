from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import login,authenticate,logout, update_session_auth_hash
from django.contrib import messages
#! admin; admin@admin.com, pw:1234 || gokhanbyk; gokhan@gokhan.com, pw: şifre123 || kullanici; kullanici@kullanici.com, pw:şifre1234
# Create your views here.
#! LOGİN
def login_view(request):

    if request.user.is_authenticated:
        messages.success(request,'Giriş Başarılı!')
        return redirect('index_page')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            username = User.objects.get(email = email).username

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request,user)
                messages.success(request,'Giriş Başarılı!')
                return redirect('index_page')
            else:
                return render(request, 'user/login.html', {
                    'form': form,
                })
        else:
            messages.warning(request,'Bilgilerinizi Gözden Geçirin!')
            return redirect(request, 'user/login.html', {
                'form': form,
            })
    else:
        form = UserLoginForm()
        return render(request, 'user/login.html', {
            'form': form,
        })
#! LOGİN
   
#? REGİSTER
def register_view(request):

    if request.user.is_authenticated:

        return redirect('index_page')

    if request.method == 'POST':
        form = Register(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username = username, password = password)
            login(request,user)
            messages.info(request,'Aramıza Hoşgeldiniz! :)')
            return redirect('index_page')
        else:
            form = Register()
            return render(request,'user/register.html', {
                'form': form,
            })

    form = Register()
    return render(request, 'user/register.html', {
        'form':form,
    })
#? REGİSTER

#* CHANGE-PASSWORD
def change_password_view(request):

    if not request.user.is_authenticated:
        return redirect('index_page')
    
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