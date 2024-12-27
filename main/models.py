from django.db import models
from django.core.validators import MinValueValidator

class ActivityCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Highlight(models.Model):
    text = models.CharField(max_length=50) 

    def __str__(self):
        return self.text

class Activities(models.Model):
    title = models.CharField(max_length=225)
    Where = models.CharField(max_length=225,help_text="Eter the Activity Place")
    description = models.TextField(help_text="Enter the Avtivity Description")
    highlights = models.ManyToManyField(Highlight, blank=True) 
    places = models.IntegerField(default=1,validators=[MinValueValidator(1)])
    category = models.ForeignKey( ActivityCategory, on_delete=models.CASCADE, related_name="activities")
    price = models.IntegerField(default=0,validators=[MinValueValidator(0)], help_text="enter teh price Activity")
    image = models.ImageField(upload_to='backgrounds/',null=True) 

    def __str__(self):
        return self.title
