from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify  

# Create your models here.

VERSIONS = (
    (11.0 ,11.0 ),
    (12.0 ,12.0 ),
    (13.0 ,13.0 ),
    (14.0 ,14.0 ),
    (15.0 ,15.0 ),
    
    )

class Apps(models.Model):

    name = models.CharField(max_length=100,blank=True,null=True)
    versions = models.FloatField( choices=VERSIONS ,blank=True,null=True)
    youtube_link = models.CharField(max_length=100,blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    technical_name = models.CharField(max_length=100,blank=True,null=True)
    is_premium = models.BooleanField(default=True,blank=True,null=True)
    is_service = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):

        return self.name
class Payments(models.Model):

    customer_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    is_paid = models.BooleanField(default = False)
    app = models.ForeignKey(Apps , on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    


