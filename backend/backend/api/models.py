from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=24)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=36)

    def __str__(self):
        return self.username