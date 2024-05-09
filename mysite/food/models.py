from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.name
    # 可以用name的值顯示
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=4)
    # 上面的default是指在建立外鍵之前就已經存在的品項，就當作是pk=1的User建立的
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="test")
    price = models.FloatField()
    img = models.CharField(max_length=500, 
                           default="https://p.kindpng.com/picc/s/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.png")
    
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    # 讓django在執行的時候，url可以知道要redirect到哪邊