from django.db import models
import datetime


class Category(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=10, default="culture")
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to ='img/', default="img/empty.png")
    content = models.TextField()
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime(year=2024, month=1, day=1))
    
    def __str__(self):
        return self.title
