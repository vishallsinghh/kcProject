from django.shortcuts import render,redirect
from .models import *
import stripe
from datetime import datetime, timedelta
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.


stripe.api_key = 'sk_test_51KdAK5SIiaymke9Xm9Nic9lnVGhimeNslzc9UPyOrDaNhoLpRTgdMk2aR9m0j4bGXHn9lG7F0DQ0EmxQFCmRWh6B00ReTOWmXR'


def checkout(request):

    if request.method == 'POST':

        print(request.POST.get('app_or_service'))
        app_or_service = Apps.objects.get(id = int(request.POST.get('app_or_service')))

        payment = Payments.objects.create(**{

                                          'email' : request.POST.get('email'),
                                          'customer_name' : request.POST.get('name'),
                                          'app': app_or_service,
                                          'amount' : request.POST.get('service_amount') if app_or_service.is_service else app_or_service.price,
                                          'description' : request.POST.get('description') if app_or_service.is_service else app_or_service.name


                                          })
       
        session=stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=[{
	      'price_data': {
	        'currency': 'inr',
	        'product_data': {
	          'name': app_or_service.name,
	        },
	        'unit_amount': int(payment.amount)*100,
	      },
	      'quantity': 1,
	    }],
	    mode='payment',

	    success_url = "http://127.0.0.1:8000/payment/success?session_id={CHECKOUT_SESSION_ID}",
	    cancel_url='http://127.0.0.1:8000/payment/cancel',
	    client_reference_id=payment.id
	    )
        return redirect(session.url, code=303)
    
    context= {
        "apps": Apps.objects.all(),
        "service_id": Apps.objects.filter(name = 'Service' ,is_service = True).first().id

    }
    return render(request, 'payment.html',context = context)

def stripe_success(request):

    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    payment_id = session.client_reference_id
    
    payment = Payments.objects.get(id = payment_id)
    payment.is_paid = True
    payment.save()

    return render(request, 'success.html')

def stripe_cancel(request):
    
    return render(request, 'cancel.html')



