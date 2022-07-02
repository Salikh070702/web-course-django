from django.db import models

from distutils.command.upload import upload
from django.db import models
from unicodedata import category
# Create your models here.

class Carusel(models.Model):
    titel = models.CharField("Nomi", max_length=200)
    image = models.ImageField("Rasim", upload_to='carusel/')

    class Meta:
        verbose_name = "Carusel"
        verbose_name_plural = "Carusel"

    def __str__(self):
        return self.titel

from distutils.command.upload import upload
from django.db import models
from unicodedata import category
  
class ImgCategory(models.Model):
    name = models.CharField("Kategoriya", max_length=255)

    class Meta:
        verbose_name = "kategoriya"
        verbose_name_plural = "Rasm kategoriyalari"

    def str(self) -> str:
        return self.name


class Gallery(models.Model):
    category = models.ForeignKey(
        ImgCategory,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    title = models.CharField("nomi", max_length=255, blank=True)
    image = models.ImageField("rasm", upload_to="images/")

    class Meta:
        ordering = ('id',)
        verbose_name = "rasm"
        verbose_name_plural = "Rasmlar"

    def str(self) -> str:
        return f"{self.id} - rasm"