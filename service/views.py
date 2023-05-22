from django.shortcuts import render
from .models import *
from django.http import HttpResponse, request
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import FileResponse
from requests import get
from datetime import datetime,date
import json
from django.shortcuts import render,redirect
from pages.models import Product


class index(View):
	def get(self,request,*args,**kwargs):
		ip = request.META.get('HTTP_X_REAL_IP')
		pk = self.kwargs['pk']
		if Statfile.objects.filter(pk=pk).exists():
			file = Statfile.objects.get(pk=pk)
		else:	
			return redirect("https://techneith.com/")	
		today = date.today()
		if StatfileCount.objects.filter(Statfile=file,ip=ip,when_add__year=today.year,when_add__month=today.month,when_add__day=today.day).exists() == False:
			url = f"https://ipapi.co/{ip}/json/"
			loc = get(url)
			data = loc.json()
			count=StatfileCount.objects.create(Statfile=file,ip=data['ip'])
#			count.meta=json.dumps(request.META)
#			count.headers=json.dumps(request.headers)
			count.version=data['version']
			count.city=data['city']
			count.region=data['region']
			count.region_code=data['region_code']
			count.country_code=data['country_code']
			count.country_code_iso3=data['country_code_iso3']
			count.country_name=data['country_name']
			count.country_capital=data['country_capital']
			count.country_tld=data['country_tld']
			count.continent_code=data['continent_code']
			count.in_eu=data['in_eu']
			count.postal=data['postal']
			count.latitude=data['latitude']
			count.longitude=data['longitude']
			count.timezone=data['timezone']
			count.utc_offset=data['utc_offset']
			count.country_calling_code=data['country_calling_code']
			count.currency=data['currency']
			count.currency_name=data['currency_name']
			count.country_area=data['country_area']
			count.save()
		else:
			sfc=StatfileCount.objects.filter(Statfile=file,ip=ip,when_add__year=today.year,when_add__month=today.month,when_add__day=today.day).last()
			sfc.request_count+=1
			sfc.save()
		return FileResponse(file.file)



class GetPhoto(View):
	def get(self,request,*args,**kwargs):
		ip = request.META.get('HTTP_X_REAL_IP')
		slug = self.kwargs['slugname']
		if Statfile.objects.filter(slug=slug).exists():
			file = Statfile.objects.get(slug=slug)
		else:	
			return redirect("https://techneith.com/")	
		today = date.today()
		if StatfileCount.objects.filter(Statfile=file,ip=ip,when_add__year=today.year,when_add__month=today.month,when_add__day=today.day).exists() == False:
			url = f"https://ipapi.co/{ip}/json/"
			loc = get(url)
			data = loc.json()
			count=StatfileCount.objects.create(Statfile=file,ip=ip)
			#count=StatfileCount.objects.create(Statfile=file,ip=data['ip'])
#			count.meta=json.dumps(request.META)
#			count.headers=json.dumps(request.headers)
			#count.version=data['version']
			count.city=data['city']
			#count.region=data['region']
			#count.region_code=data['region_code']
			#count.country_code=data['country_code']
			#count.country_code_iso3=data['country_code_iso3']
			count.country_name=data['country_name']
			#count.country_capital=data['country_capital']
			#count.country_tld=data['country_tld']
			#count.continent_code=data['continent_code']
			#count.in_eu=data['in_eu']
			#count.postal=data['postal']
			#count.latitude=data['latitude']
			#count.longitude=data['longitude']
			#count.timezone=data['timezone']
			#count.utc_offset=data['utc_offset']
			#count.country_calling_code=data['country_calling_code']
			#count.currency=data['currency']
			#count.currency_name=data['currency_name']
			#count.country_area=data['country_area']
			count.save()
		else:
			sfc=StatfileCount.objects.filter(Statfile=file,ip=ip,when_add__year=today.year,when_add__month=today.month,when_add__day=today.day).last()
			sfc.request_count+=1
			sfc.save()
		return FileResponse(file.file)


def get_visitor(request,slug,*args,**kwargs):
		ip = request.META.get('HTTP_X_REAL_IP')
		if not ip:
			return False
		if Product.objects.filter(technical_name=slug).exists():
			file = Product.objects.get(technical_name=slug)
		else:	
			return False	
		today = date.today()
		if WebStatfileCount.objects.filter(Myproduct=file,ip=ip,when_add__year=today.year,when_add__month=today.month,when_add__day=today.day).exists() == False:
			url = f"https://ipapi.co/{ip}/json/"
			loc = get(url)
			data = loc.json()
			count=WebStatfileCount.objects.create(Myproduct=file,ip=data['ip'])
#			count.meta=json.dumps(request.META)
#			count.headers=json.dumps(request.headers)
			count.version=data['version']
			count.city=data['city']
			count.region=data['region']
			count.region_code=data['region_code']
			count.country_code=data['country_code']
			count.country_code_iso3=data['country_code_iso3']
			count.country_name=data['country_name']
			count.country_capital=data['country_capital']
			count.country_tld=data['country_tld']
			count.continent_code=data['continent_code']
			count.in_eu=data['in_eu']
			count.postal=data['postal']
			count.latitude=data['latitude']
			count.longitude=data['longitude']
			count.timezone=data['timezone']
			count.utc_offset=data['utc_offset']
			count.country_calling_code=data['country_calling_code']
			count.currency=data['currency']
			count.currency_name=data['currency_name']
			count.country_area=data['country_area']
			count.save()
		else:
			sfc=WebStatfileCount.objects.filter(Myproduct=file,ip=ip,when_add__year=today.year,when_add__month=today.month,when_add__day=today.day).last()
			sfc.request_count+=1
			sfc.save()
		return True
