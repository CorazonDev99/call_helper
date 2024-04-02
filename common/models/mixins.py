from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseDictModelMixin(models.Model):
    code = models.CharField("Kod", max_length=16, primary_key=True)
    name = models.CharField('Назапние', max_length=32, )
    sort = models.PositiveSmallIntegerField('Сортировка',)
    is_active = models.BooleanField('Активность', default=True)

    class Meta:
        ordering = ('sort',)
        abstract = True

    def __str__(self):
        return f'{self.code} ({self.name})'

