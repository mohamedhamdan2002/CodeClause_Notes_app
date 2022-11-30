from django.db import models
from django.urls import reverse

# Create your models here.

class Notes(models.Model):
    title=models.CharField(max_length=500,null=True,blank=True)
    notes=models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # new
        return reverse("note_details", args=[str(self.id)])