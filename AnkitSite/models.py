from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# project model table
class Project(models.Model):
    name = models.CharField(max_length=200)
    project_link = models.URLField(max_length=200)
    project_image = CloudinaryField('image')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    click_count = models.IntegerField(default=0)
    
    # Relation to Category 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return f'{self.name} | views : {self.click_count}'