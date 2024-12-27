from django.db import models
from django.core.validators import MinValueValidator

class ActivityCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Activities(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(help_text="Enter the Avtivity Description")
    category = models.ForeignKey( ActivityCategory, on_delete=models.CASCADE, related_name="activities")
    price = models.IntegerField(default=0,validators=[MinValueValidator(0)], help_text="enter teh price Activity")
    def __str__(self):
        return self.title
