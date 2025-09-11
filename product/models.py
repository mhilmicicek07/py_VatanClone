from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Kategori(models.Model):
    kategori_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.kategori_name

class Urun(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    urun_name = models.CharField(max_length=200)
    urun_description = models.TextField(max_length=250)
    urun_price = models.DecimalField(max_digits=10, decimal_places=2)
    urun_image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    urun_category = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    urun_slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.urun_slug:
            base_slug = slugify(self.urun_name)
            slug = base_slug or "urun"
            counter = 1
            while Urun.objects.filter(urun_slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f"{base_slug}-{counter}"
            self.urun_slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.urun_name