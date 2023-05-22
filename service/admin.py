from django.contrib import admin
from .models import *
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from pages.models import Product

# Register your models here.



@admin.register(Statfile)
class StatFileAdmin(admin.ModelAdmin):
	list_display = ("id","slug","name","file","TotolCount","TodayCount","CurrentMonthCount","LastMonthCount")
	search_fields = ('name',)
	def TotolCount(self,obj):
		return StatfileCount.objects.filter(Statfile=obj).count()
	def TodayCount(self,obj):
		today = date.today()		
		CTF = StatfileCount.objects.filter(Statfile=obj,when_add__year=today.year,when_add__month=today.month,when_add__day=today.day).count()
		return CTF
	def CurrentMonthCount(self,obj):
		today = date.today()		
		CTF = StatfileCount.objects.filter(Statfile=obj,when_add__year=today.year,when_add__month=today.month).count()
		return CTF
	def LastMonthCount(self,obj):
		today = date.today()-relativedelta(month=1)
		CTF = StatfileCount.objects.filter(Statfile=obj,when_add__year=today.year,when_add__month=today.month).count()
		return CTF	
			
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ("id","name","TotolCount","TodayCount","CurrentMonthCount","LastMonthCount")
	search_fields = ('name',)
	def TotolCount(self,obj):
		return WebStatfileCount.objects.filter(Myproduct=obj).count()
	def TodayCount(self,obj):
		today = date.today()		
		CTF = WebStatfileCount.objects.filter(Myproduct=obj,when_add__year=today.year,when_add__month=today.month,when_add__day=today.day).count()
		return CTF
	def CurrentMonthCount(self,obj):
		today = date.today()		
		CTF = WebStatfileCount.objects.filter(Myproduct=obj,when_add__year=today.year,when_add__month=today.month).count()
		return CTF
	def LastMonthCount(self,obj):
		today = date.today()-relativedelta(month=1)
		CTF = WebStatfileCount.objects.filter(Myproduct=obj,when_add__year=today.year,when_add__month=today.month).count()
		return CTF	

@admin.register(StatfileCount)
class StatfileCountAdmin(admin.ModelAdmin):
	list_display = ("Name","when_add","ip","city","country_name","country_capital","request_count","latitude","longitude")
	list_filter = ("Statfile","when_add","city","country_name")
	def Name(self,obj):
		return obj.Statfile.name

@admin.register(WebStatfileCount)
class StatfileCountAdmin(admin.ModelAdmin):
	list_display = ("Name","when_add","ip","city","country_name","request_count")
	list_filter = ("Myproduct","when_add","city","country_name")
	def Name(self,obj):
		return obj.Myproduct.name






@admin.register(tablueFile)
class tablueFileAdmin(admin.ModelAdmin):
	list_display = ("id","slug","name","file")
	search_fields = ('name',"category")
	list_filter = ("category",)

admin.site.register(MediaFile)