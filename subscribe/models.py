from django.db import models

# Create your models here.
NEWS_LETTER =[
    ('W',"Weekly"),
    ('M',"Monthly")
]

class Subscribe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    option =models.CharField(max_length=2,choices=NEWS_LETTER, default='M')

    