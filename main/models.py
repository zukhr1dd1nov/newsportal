from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = "Kategoriyalar"

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    subject = models.CharField(max_length=200)
    content = models.TextField()    
    added_at = models.DateTimeField(auto_now_add=True)