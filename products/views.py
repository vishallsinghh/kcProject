from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def getProductList(request):
    prods = ["name", 'cycle', 'bike']
    return JsonResponse(prods, safe=False)