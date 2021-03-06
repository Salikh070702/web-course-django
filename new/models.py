from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class New(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name="Muallif",
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    title = models.CharField("Sarlavha",max_length=255)
    body = models.TextField("Asosiy qisim")
    image = models.ImageField("Rasim", upload_to="news/", blank=True, null=True)
    created = models.DateTimeField("Sana", auto_now=True)

    class Meta:
        verbose_name = "yangilik"
        verbose_name_plural = "Yangiliklar"


    def __str__(self):
        return self .title

def get_absolute_url(self):
    return reverse("news:list")

    def dislike_count(self):
        return self.dislikes.count()


    def like_count(self):
        return self.likes.count()
    

class Comment(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name="Muallif",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        )
    post = models.ForeignKey(
        New,
        verbose_name="Post",
        on_delete=models.SET_NULL,
        related_name="comments",
        null=True,
        blank=True
        )  
    body = models.TextField("Izoh")
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.body[:20]}..."

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"


class Like(models.Model):
    post = models.ForeignKey(
        New,
        verbose_name="Post",
        on_delete=models.SET_NULL,
        related_name="likes",
        null=True,
        blank=True
    )  
    user = models.ForeignKey(
        User,
        verbose_name="Post",
        on_delete=models.SET_NULL,
        related_name="likes",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "yoqimli"
        verbose_name_plural = "Yoqimlilar"

    def __str__(self):
        return f"{self.user.username}ga {self.post.title} yoqdi"  


class Dislike(models.Model):
    post = models.ForeignKey(
        New,
        verbose_name="Post",
        on_delete=models.SET_NULL,
        related_name="dislikes",
        null=True,
        blank=True
    )  
    user = models.ForeignKey(
        User,
        verbose_name="Post",
        on_delete=models.SET_NULL,
        related_name="dislikes",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "yoqimsiz"
        verbose_name_plural = "Yoqimsizlar"

    def __str__(self):
        return f"{self.user.username}ga {self.post.title} yoqmadi"  