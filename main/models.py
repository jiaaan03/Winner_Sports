import uuid
from django.db import models

class News(models.Model):
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
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES, default='update')
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()