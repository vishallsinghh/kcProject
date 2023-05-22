from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import Article, Contact, TrackVisiters, Work, Product,DashboardForm, AppBuyRequest, OdooVersion, Comments,CommentReply,Page
from .smtp import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from service.views import get_visitor

def home(request):
    context = {
        'works': Work.objects.all(),
        'blogs': Article.objects.filter(featured=True).order_by('order_number'),
        'products': Product.objects.filter(featured=True).order_by('order_number')
    }
    return render(request, 'pages/home.html', context)

def contact(request):
    if request.method == "POST":
        contact = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'description': request.POST.get('description'),
        }
        contact_object = Contact.objects.create(**contact)
        msg = f'''
        Hii sir the following query came from our website.

        name : {contact.get('name')}
        email : {contact.get('email')}
        query :{contact.get('description')}
        '''
        send_mail(email='info@techneith.com',
                  subject='Query from Website', msg=msg,cc=['chandan@techneith.com'])
        return JsonResponse(data={'success': 'True'}, status=200)
    return render(request,'pages/404.html')

def comment(request,comment_type,page):
    print("\n\n\n"+str(request.POST.get('product_id')))
    if request.method == "POST":
        if comment_type == 'reply':
            reply = CommentReply(content=request.POST.get('content'))
            reply.save()
            comment = Comments.objects.get(id=request.POST.get('comment_id'))
            comment.replies.add(reply)
        else:
            comment = Comments(title= request.POST.get('title'),
                content= request.POST.get('content'),
                author= request.POST.get('author'))
            comment.save()
            if Product.objects.filter(technical_name=page).exists():
                print("\n\nproduct")
                product = Product.objects.get(id=request.POST.get('product_id'))
                product.comments.add(comment)
            elif Article.objects.filter(slug=page).exists():
                print("\nblogs")
                product = Article.objects.get(id=request.POST.get('product_id'))
                product.comments.add(comment)
                send_mail(email='chandan@techneith.com',subject='New comment on {}'.format(page), msg="{} \n from {}".format(request.POST.get('content'),request.POST.get('author')),cc=['vishalsinghalt123@gmail.com'])

                return redirect('/blogs/'+page+'/')
            else:
                print("\npage")
                product = Page.objects.get(slug=page)
                product.comments.add(comment)
                send_mail(email='chandan@techneith.com',subject='New comment on {}'.format(page), msg="{} \n from {}".format(request.POST.get('content'),request.POST.get('author')),cc=['vishalsinghalt123@gmail.com'])

                return redirect('/resources/'+page+'/')
            send_mail(email='chandan@techneith.com',subject='New comment on {}'.format(page), msg="{} \n from {}".format(request.POST.get('content'),request.POST.get('author')),cc=['vishalsinghalt123@gmail.com'])
        return redirect('/products/'+page+'/')
    return render(request,'pages/404.html')

@csrf_exempt
def dashboard_form(request):
    if request.method == "POST" or request.method == "OPTIONS" :
        contact = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'company': request.POST.get('company'),
            'data': str(request.POST.get('data')),
        }
        contact_object = DashboardForm.objects.create(**contact)
        msg = f'''
        Hi Team,
        New query for Dashboard from Website.

        name : {contact.get('name')}
        email : {contact.get('email')}
        company : {contact.get('company')}
        data :{contact.get('data')}
        '''
        send_mail(email='info@techneith.com',
                subject='Dashboard Query from Website', msg=msg,cc=['chandan@techneith.com'])
                  
        response = JsonResponse(data={'success': 'True'}, status=200)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response

def blog(request):
    all_post = Article.objects.all()
    # page = request.GET.get('page')
    # try:
    #     posts = all_post.page(page)
    # except PageNotAnInteger:
    #     posts = all_post.page(1)
    # except EmptyPage:
    #     posts = all_post.page(all_post.num_pages)
    context = {
        "articles": all_post
    }

    return render(request, 'pages/blog.html', context=context)


def blog_detail(request, slug):
    context = {
        'article': Article.objects.get(slug=slug)
    }
    if slug == "how-to-connect-odoo-with-power-bi":
        return render(request, 'pages/blogs/powerbi_blog.html',context)
    
    return render(request, 'pages/blog_detail.html', context)

def resources(request, slug):
    context = {
        'page': Page.objects.get(slug=slug)
    }
    return render(request, 'pages/resources/{}.html'.format(slug),context=context)

def checkout(request, slug):
    if request.method == "POST":
        contact = {
            'name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'company_name': request.POST.get('company_name'),
            'odoo_version': request.POST.get('odoo_version'),
            'production_url': request.POST.get('production_url'),
            'staging_url': request.POST.get('staging_url'),
        }
        return redirect('/products/odoo_power_bi_direct_connector')
    #normal
    product = Product.objects.filter(technical_name=slug).first()
    if not product :
        return redirect('/products/')
    context = {
        'product': product
    }
    return render(request, 'pages/product/checkout.html', context)


def product_page(request, slug):
    #get_visitor(request, slug)
    
    if request.method == "POST":
        print(request.POST.keys(),request.POST.values())
        if 'issue' in request.POST.keys():
            msg = f'''
                Feedback for BI Connector

                issue : {request.POST.get('issue')}
                email : {request.POST.get('email')}
                description :{request.POST.get('description')}'''
            send_mail(email='chandan@techneith.com',
                  subject="Feedback BI Connector {}".format(request.POST.get('issue')), msg=msg,cc=['info@techneith.com'])
        else:
            contact = {
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
                'odoo_product': request.POST.get('odoo_product'),
                'odoo_version': request.POST.get('odoo_version'),
            }
            #contact_object = AppBuyRequest.objects.create(**contact)
            msg = f'''
            New Demo request from Website
            name : {contact.get('name')} {request.POST.get('last_name')}
            email : {contact.get('email')}
            odoo_product :{contact.get('odoo_product')}
            odoo_version :{contact.get('odoo_version')}
            company_name : {request.POST.get('company_name')}
            company_size : {request.POST.get('company_size')}
            production url : {request.POST.get('production_url')}
            staging url : {request.POST.get('staging_url')}
            '''
            send_mail(email='chandan@techneith.com',
                    subject="Demo Request for {} from {}".format(contact.get('odoo_product'),contact.get('name')), msg=msg,cc=['info@techneith.com'])
            # all_product = Product.objects.all().order_by('order_number')
            return render(request, 'pages/payments/form_success.html')
    if slug == 'powerbiconnector':
        return redirect('/products/odoo_power_bi_direct_connector')
    product = Product.objects.filter(technical_name=slug).first()
    if not product :
        return redirect('/products/')
    similar = Product.objects.exclude(id=product.id)
    context = {
        'product': product,
        'similar':similar[:3]
    }
    if len(product.doc) == 0:
        return render(request, 'pages/product/{}.html'.format(product.technical_name), context)
    return render(request, 'pages/product/single_product.html', context)

def dashboard(request,slug):
    if request.method == "POST":
            msg = f'''
                Dashboard query from Techneith.com

                Dashboard: {request.POST.get('odoo_product')}
                email : {request.POST.get('email')}
                name :{request.POST.get('name')}'''
            send_mail(email='chandan@techneith.com',
                  subject="Power BI Dashboard Query", msg=msg,cc=['info@techneith.com'])
    return render(request, 'pages/dashboard/{}.html'.format(slug))

def pricing(request,slug):
    return render(request, 'pages/payments/pricing.html')

def buyapp(request):
    if request.method == "POST":
        contact = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'odoo_product': request.POST.get('odoo_product'),
            'odoo_version': request.POST.get('odoo_version'),
        }
        contact_object = AppBuyRequest.objects.create(**contact)
        msg = f'''
        New Purchase request for Odoo App

        name : {contact.get('name')}
        email : {contact.get('email')}
        odoo_product :{contact.get('odoo_product')}
        odoo_version :{contact.get('odoo_version')}
        '''
        
        send_mail(email='info@techneith.com',
                  subject="Buy Request for {}".format(contact.get('odoo_product')), msg=msg,cc=['chandan@techneith.com'])
        # all_product = Product.objects.all().order_by('order_number')
        return JsonResponse(data={'success': 'True'}, status=200)
    return render(request, 'pages/404.html', status=404)

# Products List
def product(request):
    odoo_version = request.GET.get('version')
    selected_version = None
    if odoo_version and not odoo_version == "All":
        prods = Product.objects.filter(odooversion__version_name=odoo_version)
        selected_version = odoo_version
    else:
        prods = Product.objects.all()
    sort_by = request.GET.get('sort')
    if sort_by == 'latest':
        all_product = prods.order_by('-creation_time','order_number')
    elif sort_by == 'highest_price':
        all_product = prods.order_by('-price','order_number')
    elif sort_by == 'popular':
        all_product = prods.order_by('-total_sales','order_number')
    elif sort_by == 'ratings':
        all_product = prods.order_by('-star_rating','order_number')
    elif sort_by == 'lowest_price':
        all_product = prods.order_by('price','order_number')
    else:
        all_product = prods.order_by('order_number','-total_sales')
    
    od_vr = [ov.version_name for ov in OdooVersion.objects.all()]
    context = {
        "products": all_product,
        "all_versions": od_vr,
        "selected_version": selected_version if selected_version else "All"
    }
    return render(request, 'pages/products.html', context)

def livedashboards(request,app,slug):
    return render(request, 'pages/livedashboards/{}/{}.html'.format(app,slug))

# product pages
def testing(request,slug):
        return render(request, 'pages/testing/{}.html'.format(slug))

def bi_connector(request):
    return render(request, 'pages/connector.html')

def redirect_to_bi_connector(request):
    response = redirect('/products/powerbiconnector/')
    return response

def docket(request):
    return render(request, 'pages/docket.html')

def sales_dashboard(request):
    return render(request, 'pages/sales-dash.html')

def error_404_view(request, exception):
    # response.status_code = 404
    return render(request,'pages/404.html')

def error_404(request, exception):
    return render(request, 'pages/404.html', status=404)

def demodashboard(request):
    return render(request, 'pages/demodashboard.html')

def customdemodashboard(request):
    return render(request, 'pages/demoform.html')

def tabluedev(request):
    return render(request, 'pages/tabluepage.html')

# def dytest(request):
#     return render(request, 'pages/dynamic_product.html')

def about(request):
    return render(request, 'pages/team.html')

# def odoo_app_store(request):
#     email = request.GET.get('email')
#     print(email)
#     if email:
#         try:
#             obj = TrackVisiters.objects.get(email=email)
#             obj.visit_count += 1
#             obj.save()
#         except ObjectDoesNotExist:
#             obj = TrackVisiters.objects.create(
#                 **{'email': email, 'visit_count': 1})
#     return redirect("https://apps.odoo.com/apps/modules/browse?author=Techneith")

# def skucast(request):
#     return render(request, 'pages/skucast.html')