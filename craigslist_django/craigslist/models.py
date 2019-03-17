from django.db import models
from django.utils import timezone

class Category(models.Model):
  category_name = models.CharField(max_length=255)

  def __str__(self):
    return self.category_name 

class Post(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
  post_title = models.CharField(max_length=255)
  post_body = models.TextField()
  post_city = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  image = models.CharField(max_length=255)
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'{self.post_title} for ${self.price}'