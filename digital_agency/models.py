from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sendedAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    addedAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.email