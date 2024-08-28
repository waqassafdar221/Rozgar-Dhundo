from django.db import models
from django.utils.text import slugify

# Create your models here.
class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    zip = models.CharField(max_length=20)
     
    def __str__(self):
        return self.city
class Skills(models.Model):
    name = models.CharField(max_length=200)

class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=50, unique=True)
    location = models.OneToOneField(Location,on_delete=models.CASCADE,null=True)
    author =models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    skill = models.ManyToManyField(Skills)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args,**kwargs)

    def __str__(self):
        return self.title
    