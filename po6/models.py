from django.db import models
from django.contrib.auth.models import User


class Redistribution(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Техпередел'
        verbose_name_plural = 'Техпеределы'

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic_name = models.CharField(max_length=150, verbose_name='Отчество', blank=True)
    redistribution = models.ForeignKey(Redistribution, on_delete=models.CASCADE, null=True)
    addr = models.CharField(max_length=64, verbose_name='Адрес', blank=False, default='0.0.0.0')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def get_full_name(self):
        return f'{self.user.last_name} {self.user.first_name[:1]}. {self.patronymic_name[:1]}.'

    def __str__(self):
        return f'{self.user.last_name}'
