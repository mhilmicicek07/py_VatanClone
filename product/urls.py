from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_page'),
    path('<int:kategori_id>/', detay_view, name="detay_page"),
    path('urun/<slug:urun_slug>/', urun_detay_view, name="urun_detay"),
    path('create/', create_view, name='create_page'),
    path('delete/<slug:urun_slug>/', delete_view, name='delete_page'),
    path('edit/<slug:urun_slug>/', edit_view, name='edit_page'),
]
# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('', index_view, name='index_page'),
#     path('<int:kategori_id>/', detay_view, name="detay_page"),
#     path('<int:kategori_id>/<slug:urun_slug>/', urun_detay_view, name="urun_detay_page"),
#     path('create/', create_view, name='create_page'),
#     path('delete/<slug:urun_slug>/', delete_view, name='delete_page'),
#     path('edit/<slug:urun_slug>/', edit_view, name='edit_page'),
# ]
