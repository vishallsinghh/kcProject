from django.shortcuts import render
import stripe
from django.conf import settings # new
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
from django.views.generic.base import TemplateView
from django.http.response import JsonResponse, HttpResponse
from pages.smtp import send_mail
import json
import requests

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'https://www.techneith.com/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        pay_form = json.loads(request.GET.get('body'))
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create
            
            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                customer_email= pay_form['email'],
                metadata=pay_form,
                line_items=[
                    {
                        'quantity': 1,
                        'price': pay_form['stripe_price'],
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

class SuccessView(TemplateView):
    template_name = 'pages/payments/success.html'


class CancelledView(TemplateView):
    template_name = 'pages/payments/cancelled.html'


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        payload = json.loads(payload.decode('utf8').replace("'", '"'))
        server_message = 'None'
        msg = f'''
                Purchase on website
                {payload}'''
        send_mail(email='chandan@techneith.com',
                subject="Purchase on Website", msg=msg,cc=['info@techneith.com'])

        odoopost = {"customer_name":payload['data']['object']['metadata']['first_name']+' '+payload['data']['object']['metadata']['last_name'],
            "customer_email":payload['data']['object']['metadata']['email'],
            "customer_company":payload['data']['object']['metadata']['company_name'],
            "odoo_version":payload['data']['object']['metadata']['odoo_version'],
            "product_technical_name":payload['data']['object']['metadata']['odoo_crm_tech_name'],
            "current_price":int(payload['data']['object']['amount_total'])/100,
            "qty":1,
            "production_url" : payload['data']['object']['metadata']['production_url'],
            "staging_url":payload['data']['object']['metadata']['staging_url']}
        r = requests.post('https://odoo.techneith.com/sales/', data=odoopost)

        return HttpResponse(status=200)
    msg = f'''
                Some checkout activity on website
                {payload}'''
    send_mail(email='chandan@techneith.com',
            subject="Checkout activity Website", msg=msg,cc=['info@techneith.com'])
    return HttpResponse(status=200)