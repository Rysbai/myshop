from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    user = models.OneToOneField(User, verbose_name="Клиент")
    city = models.CharField(max_length=100, verbose_name="Город", default="Бишкек")
    phone = models.IntegerField()
