from django.db import models

# Create your models here.
class Holiday(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    day = models.DateField()
    international = models.BooleanField(default=False)
    worldwide = models.BooleanField(default=False)
    on_russian = models.BooleanField(default=False)
    other_country = models.BooleanField(default=False)
    fill_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)