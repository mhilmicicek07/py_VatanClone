from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Kategori(models.Model):
    kategori_name = models.CharField(max_length=50)
    # kategori_image = models.FileField(upload_to='kategori_images')
    # kategori_slug = models.SlugField(unique=True, blank=True)

    # def save(self, *args, **kwargs):
    #     self.kategori_slug = slugify(self.kategori_name)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.kategori_name

class Urun(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    urun_name = models.CharField(max_length=100)
    urun_description = models.CharField(max_length=250)
    urun_price = models.DecimalField(max_digits=10, decimal_places=2)
    urun_image = models.CharField(max_length=500)

    urun_category = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)

    urun_slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.urun_slug = slugify(self.urun_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.urun_name
