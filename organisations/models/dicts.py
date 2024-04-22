from django.contrib.auth import get_user_model
from django.db import models

from common.models.mixins import BaseDictModelMixin

User = get_user_model()


class Position(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


