from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator

from .models import Urun, Kategori
from .forms import UrunEkle


def index_view(request):
    kategoriler = Kategori.objects.all()
    urunler = Urun.objects.select_related("urun_category", "user").all().order_by("-id")
    paginator = Paginator(urunler, 12)
    page = request.GET.get("page")
    urunler = paginator.get_page(page)
    return render(request, "product/index.html", {"urunler": urunler, "kategoriler": kategoriler})


def detay_view(request, kategori_id):
    kategoriler = Kategori.objects.all()
    qs = Urun.objects.filter(urun_category_id=kategori_id).select_related("urun_category", "user")
    paginator = Paginator(qs.order_by("-id"), 12)
    page = request.GET.get("page")
    urunler = paginator.get_page(page)
    return render(request, "product/detay.html", {"urunler": urunler, "kategoriler": kategoriler})


def urun_detay_view(request, urun_slug):
    kategoriler = Kategori.objects.all()
    urun = get_object_or_404(
        Urun.objects.select_related("urun_category", "user"), urun_slug=urun_slug
    )
    return render(request, "product/urun-detay.html", {"urun": urun, "kategoriler": kategoriler})


@login_required
def create_view(request):
    kategoriler = Kategori.objects.all()
    if request.method == "POST":
        form = UrunEkle(request.POST, request.FILES)
        if form.is_valid():
            urun = form.save(commit=False)
            urun.user = request.user
            urun.save()
            messages.success(request, "Ürün Başarıyla Eklendi!")
            return redirect("index_page")
    else:
        form = UrunEkle()
    return render(request, "product/create.html", {"form": form, "kategoriler": kategoriler})


@login_required
def edit_view(request, urun_slug):
    urun = get_object_or_404(Urun, urun_slug=urun_slug)
    if urun.user_id != request.user.id:
        raise PermissionDenied
    if request.method == "POST":
        form = UrunEkle(request.POST, request.FILES, instance=urun)
        if form.is_valid():
            form.save()
            messages.info(request, "Ürün Güncellendi!")
            return redirect("index_page")
    else:
        form = UrunEkle(instance=urun)
    return render(request, "product/edit.html", {"urun": urun, "form": form})


@login_required
def delete_view(request, urun_slug):
    urun = get_object_or_404(Urun, urun_slug=urun_slug)
    if urun.user_id != request.user.id:
        raise PermissionDenied
    if request.method == "POST":
        urun.delete()
        messages.warning(request, "Ürün Silindi!")
        return redirect("index_page")
    return render(request, "product/delete.html", {"urun": urun})
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import PermissionDenied
# from django.core.paginator import Paginator

# from .models import Urun, Kategori
# from .forms import UrunEkle


# def index_view(request):
#     kategoriler = Kategori.objects.all()
#     urunler = Urun.objects.select_related("urun_category", "user").all().order_by("-id")
#     paginator = Paginator(urunler, 12)
#     page = request.GET.get("page")
#     urunler = paginator.get_page(page)
#     return render(request, "product/index.html", {"urunler": urunler, "kategoriler": kategoriler})


# def detay_view(request, kategori_id):
#     kategoriler = Kategori.objects.all()
#     qs = Urun.objects.filter(urun_category_id=kategori_id).select_related("urun_category", "user")
#     paginator = Paginator(qs.order_by("-id"), 12)
#     page = request.GET.get("page")
#     urunler = paginator.get_page(page)
#     return render(request, "product/detay.html", {"urunler": urunler, "kategoriler": kategoriler})


# def urun_detay_view(request, kategori_id, urun_slug):
#     kategoriler = Kategori.objects.all()
#     urun = get_object_or_404(
#         Urun.objects.select_related("urun_category", "user"), urun_slug=urun_slug
#     )
#     return render(request, "product/urun-detay.html", {"urun": urun, "kategoriler": kategoriler})


# @login_required
# def create_view(request):
#     kategoriler = Kategori.objects.all()
#     if request.method == "POST":
#         form = UrunEkle(request.POST, request.FILES)
#         if form.is_valid():
#             urun = form.save(commit=False)
#             urun.user = request.user
#             urun.save()
#             messages.success(request, "Ürün Başarıyla Eklendi!")
#             return redirect("index_page")
#     else:
#         form = UrunEkle()
#     return render(request, "product/create.html", {"form": form, "kategoriler": kategoriler})


# @login_required
# def edit_view(request, urun_slug):
#     urun = get_object_or_404(Urun, urun_slug=urun_slug)
#     if urun.user_id != request.user.id:
#         raise PermissionDenied
#     if request.method == "POST":
#         form = UrunEkle(request.POST, request.FILES, instance=urun)
#         if form.is_valid():
#             form.save()
#             messages.info(request, "Ürün Güncellendi!")
#             return redirect("index_page")
#     else:
#         form = UrunEkle(instance=urun)
#     return render(request, "product/edit.html", {"urun": urun, "form": form})


# @login_required
# def delete_view(request, urun_slug):
#     urun = get_object_or_404(Urun, urun_slug=urun_slug)
#     if urun.user_id != request.user.id:
#         raise PermissionDenied
#     if request.method == "POST":
#         urun.delete()
#         messages.warning(request, "Ürün Silindi!")
#         return redirect("index_page")
#     return render(request, "product/delete.html", {"urun": urun})

# # from django.shortcuts import render, redirect,get_object_or_404
# # from .models import *
# # from .forms import *
# # from django.contrib import messages

# # # Create your views here.
# # def index_view(request):

# #     kategoriler = Kategori.objects.all()
    
# #     urunler = Urun.objects.all()
    
# #     return render(request, 'product/index.html', {
# #         'urunler': urunler,
# #         'kategoriler': kategoriler,
# #     })


# # def detay_view(request, kategori_id):

# #     kategoriler = Kategori.objects.all()
# #     urunler = Urun.objects.filter(urun_category_id = kategori_id, user= request.user)
    
# #     return render(request, 'product/detay.html', {
# #         'urunler': urunler,
# #         'kategoriler': kategoriler,
# #     })

# # def urun_detay_view(request, kategori_id, urun_slug):
    
# #     kategoriler = Kategori.objects.all()
# #     urun = Urun.objects.filter(urun_slug = urun_slug)

# #     return render(request,'product/urun-detay.html',{
# #         'kategoriler':kategoriler,
# #         'urun': urun,
# #     })

# # def create_view(request):

# #     kategoriler = Kategori.objects.all()
    
# #     if request.method == 'POST':
# #         form = UrunEkle(request.POST) #request.FILES

# #         if form.is_valid():
# #             # form.save()
# #             urun = form.save(commit=False)
# #             urun.user = request.user
# #             urun.save()
# #             messages.success(request, 'Ürün Başarıyla Eklendi!')
# #             return redirect('index_page')
# #     else:
# #         form = UrunEkle()
# #         return render(request, 'product/create.html', {
# #            'form': form,
# #            'kategoriler': kategoriler,
# #         })
    
# # def delete_view(request, urun_slug):

# #     kategoriler = Kategori.objects.all()

# #     urun = get_object_or_404(Urun, urun_slug = urun_slug)

# #     if request.method == 'POST':
# #         urun.delete()
# #         messages.warning(request, 'Ürün Silindi!')
# #         return redirect('index_page')
# #     else:
# #         return render(request, 'product/delete.html', {
# #             'urun': urun,
# #             'kategoriler': kategoriler,
# #         })
    
# # def edit_view(request, urun_slug):
    
# #     urun = get_object_or_404(Urun, urun_slug = urun_slug)

# #     if request.method == 'POST':
# #         form = UrunEkle(request.POST, instance=urun) #request.FILES

# #         if form.is_valid():
# #             # form.save()
# #             urun = form.save(commit=False)
# #             urun.user = request.user
# #             urun.save()
# #             messages.info(request,'Ürün Güncellendi!')
# #             return redirect('index_page')
# #     else:
# #         form = UrunEkle(instance=urun)
# #         return render(request, 'product/edit.html', {
# #             'urun': urun,
# #             'form': form,
# #         })
    