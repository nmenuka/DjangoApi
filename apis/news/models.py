from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.
class News(models.Model):
    NEWS_CATEGORY=(('1',"Political"),('2',"Sport"),('3',"Entertainments"))
    title = models.CharField(max_length=300)
    content = models.TextField()
    avatar = models.ImageField(upload_to="uploads", null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    reported_at = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=2, choices=NEWS_CATEGORY)

    class Meta:
        verbose_name_plural="Newses"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail-news", kwargs={"pk":self.pk })
    
    
class NewsComment(models.Model):
    article = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.content