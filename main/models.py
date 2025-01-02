from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
