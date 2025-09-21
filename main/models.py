from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('baju jersey', 'Baju jersey'),
        ('celana', 'Celana'),
        ('sepatu', 'Sepatu'),
        ('bola', 'Bola'),
        ('botol minum', 'Botol Minum'),
        ('kaos kaki', 'Kaos kaki'),
        ('tas sepatu', 'Tas Sepatu'),
    ]

    BRAND_CHOICES = [
        ('nike', 'Nike'),
        ('adidas', 'Adidas'),
        ('puma', 'Puma'),
        ('new balance', 'New Balance'),
        ('asics', 'Asics'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='baju jersey')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES, default='nike')
    