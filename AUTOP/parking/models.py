from unittest.util import _MAX_LENGTH
from django.db import models


class P_parking(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.title