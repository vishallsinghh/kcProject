
from django.urls import path,include
from .views import *

urlpatterns = [
    
   
   
    path('checkout/' ,checkout , name="checkout"),
    path('payment/success/' , stripe_success , name="success"),
    path('payment/cancel/' , stripe_cancel , name="cancel")
  
    
  
]