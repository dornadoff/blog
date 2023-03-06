from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField()
    matn = models.CharField(max_length=1000)
    rasm = models.FileField()

class Intervyu(models.Model):
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField()
    video_url = models.TextField()