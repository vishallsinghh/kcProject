from django.db import models
from pages.models import Product

# Create your models here.


class Statfile(models.Model):
	slug = models.SlugField(max_length = 1000,unique=True,default="")
	name=models.CharField(default="",unique=True,max_length=1000)
	file=models.ImageField(default="noimage.jpg",upload_to='Statfile')
	def __str__(self):
		return str(self.id) + "-"+self.name



class StatfileCount(models.Model):
	Statfile=models.ForeignKey(Statfile,on_delete=models.CASCADE)
	when_add=models.DateTimeField(auto_now=True,editable=True)
	meta = models.JSONField(default="")
	headers = models.JSONField(default="")
	ip = models.CharField(max_length=200,default="")
	version = models.CharField(max_length=200,default="")
	city = models.CharField(max_length=200,default="")
	region = models.CharField(max_length=200,default="")
	region_code = models.CharField(max_length=200,default="")
	country_code = models.CharField(max_length=200,default="")
	country_code_iso3 = models.CharField(max_length=200,default="")
	country_name = models.CharField(max_length=200,default="")
	country_capital = models.CharField(max_length=200,default="")
	country_tld = models.CharField(max_length=200,default="")
	continent_code = models.CharField(max_length=200,default="")
	in_eu = models.CharField(max_length=200,default="")
	postal = models.CharField(max_length=200,default="")
	latitude = models.CharField(max_length=200,default="")
	longitude = models.CharField(max_length=200,default="")
	timezone = models.CharField(max_length=200,default="")
	utc_offset = models.CharField(max_length=200,default="")
	country_calling_code = models.CharField(max_length=200,default="")
	currency = models.CharField(max_length=200,default="")
	currency_name = models.CharField(max_length=200,default="")
	language = models.CharField(max_length=200,default="")
	country_area = models.CharField(max_length=200,default="")
	request_count = models.IntegerField(default=0)
	def __str__(self):
		return str(self.pk)+ " " + self.Statfile.name

class WebStatfileCount(models.Model):
	Myproduct=models.ForeignKey(Product,on_delete=models.PROTECT)
	when_add=models.DateTimeField(auto_now=True,editable=True)
	meta = models.JSONField(default="")
	headers = models.JSONField(default="")
	ip = models.CharField(max_length=200,default="")
	version = models.CharField(max_length=200,default="")
	city = models.CharField(max_length=200,default="")
	region = models.CharField(max_length=200,default="")
	region_code = models.CharField(max_length=200,default="")
	country_code = models.CharField(max_length=200,default="")
	country_code_iso3 = models.CharField(max_length=200,default="")
	country_name = models.CharField(max_length=200,default="")
	country_capital = models.CharField(max_length=200,default="")
	country_tld = models.CharField(max_length=200,default="")
	continent_code = models.CharField(max_length=200,default="")
	in_eu = models.CharField(max_length=200,default="")
	postal = models.CharField(max_length=200,default="")
	latitude = models.CharField(max_length=200,default="")
	longitude = models.CharField(max_length=200,default="")
	timezone = models.CharField(max_length=200,default="")
	utc_offset = models.CharField(max_length=200,default="")
	country_calling_code = models.CharField(max_length=200,default="")
	currency = models.CharField(max_length=200,default="")
	currency_name = models.CharField(max_length=200,default="")
	language = models.CharField(max_length=200,default="")
	country_area = models.CharField(max_length=200,default="")
	request_count = models.IntegerField(default=0)
	def __str__(self):
		return str(self.pk)+ " " + self.Myproduct.name



class tablueFile(models.Model):
	category = models.CharField(default="",max_length=1000)
	slug = models.SlugField(max_length = 1000,unique=True,default="")
	name=models.CharField(default="",unique=True,max_length=1000)
	file=models.ImageField(default="noimage.jpg",upload_to='tabluefile')
	def __str__(self):
		return str(self.id) + "-"+self.name

class MediaFile(models.Model):
	file=models.FileField(upload_to='tabluefile')
	def __str__(self):
		return str(self.file)