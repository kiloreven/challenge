from django.db import models

class Config(models.Model):
    welcometext = models.TextField(blank=True)
    eventname = models.CharField(max_length=256)
    active = models.BooleanField(default=False)
