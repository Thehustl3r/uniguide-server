from django.db import models

class Member(models.Model):
    firt_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)