# 建立sinal
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# 建立接受器
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
# sender是會觸發這個信號的model
# 當User發出post_save這個signal時，便會啟動build_profile這個function
def build_profile(sender, instance, created, **kwargs):
    # created是布林值；instance是創造出的實例
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
