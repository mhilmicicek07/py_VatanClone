from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def index_view(request):

    kategoriler = Kategori.objects.all()
    
    urunler = Urun.objects.all()
    
    return render(request, 'product/index.html', {
        'urunler': urunler,
        'kategoriler': kategoriler,
    })


def detay_view(request, kategori_id):

    kategoriler = Kategori.objects.all()
    urunler = Urun.objects.filter(urun_category_id = kategori_id, user= request.user)
    
    return render(request, 'product/detay.html', {
        'urunler': urunler,
        'kategoriler': kategoriler,
    })

def urun_detay_view(request, kategori_id, urun_slug):
    
    kategoriler = Kategori.objects.all()
    urun = Urun.objects.filter(urun_slug = urun_slug)

    return render(request,'product/urun-detay.html',{
        'kategoriler':kategoriler,
        'urun': urun,
    })

def create_view(request):

    kategoriler = Kategori.objects.all()
    
    if request.method == 'POST':
        form = UrunEkle(request.POST) #request.FILES

        if form.is_valid():
            # form.save()
            urun = form.save(commit=False)
            urun.user = request.user
            urun.save()
            messages.success(request, 'Ürün Başarıyla Eklendi!')
            return redirect('index_page')
    else:
        form = UrunEkle()
        return render(request, 'product/create.html', {
           'form': form,
           'kategoriler': kategoriler,
        })
    
def delete_view(request, urun_slug):

    kategoriler = Kategori.objects.all()

    urun = get_object_or_404(Urun, urun_slug = urun_slug)

    if request.method == 'POST':
        urun.delete()
        messages.warning(request, 'Ürün Silindi!')
        return redirect('index_page')
    else:
        return render(request, 'product/delete.html', {
            'urun': urun,
            'kategoriler': kategoriler,
        })
    
def edit_view(request, urun_slug):
    
    urun = get_object_or_404(Urun, urun_slug = urun_slug)

    if request.method == 'POST':
        form = UrunEkle(request.POST, instance=urun) #request.FILES

        if form.is_valid():
            # form.save()
            urun = form.save(commit=False)
            urun.user = request.user
            urun.save()
            messages.info(request,'Ürün Güncellendi!')
            return redirect('index_page')
    else:
        form = UrunEkle(instance=urun)
        return render(request, 'product/edit.html', {
            'urun': urun,
            'form': form,
        })
    