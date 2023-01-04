from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Categories(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    slug = models.SlugField()
    thumbnail=models.FileField(upload_to="media/thumbnail")
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("category_list")

    def __str__(self):
        return self.title
    
    def save(self):
        self.slug = slugify(self.title)
        super(Categories,self).save()
