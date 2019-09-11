from django.db import models


class User(models.Model):
    email = models.CharField(primary_key=True,max_length=100, unique=True, null=False)
