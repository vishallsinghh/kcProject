from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('buy/', views.buyapp, name='buy_app'),
    path('blogs/', views.blog, name='blog'),
    path('blogs/<str:slug>/', views.blog_detail, name='blog_detail'),
    path('resources/<str:slug>/', views.resources),
    path('products/', views.product, name='product'),
    path('pricing/<str:slug>/', views.pricing),
    path('products/checkout/<str:slug>', views.checkout),
    path('products/<str:slug>/', views.product_page, name='test'),
    path('comments/<str:comment_type>/<str:page>/', views.comment),
    path('dashboards/<str:slug>/', views.dashboard),
    path('about/', views.about),
    path('live-dashboards/<str:app>/<str:slug>/', views.livedashboards),
    path('testing-development/<str:slug>/', views.testing),



    # TODO
    path('demodashboard/', views.demodashboard , name="demodashboard"),
    path('custom-demo/dashboard/', views.customdemodashboard , name="customdemodashboard"),
    path("tabluedev/" ,views.tabluedev , name="tabluedev"),
#     path('products/docket_for_odoo/', views.docket, name='docket'),
#     path('products/powerbiconnector/', views.bi_connector, name='pages/bi_connector'),
#     path('powerbiconnector/', views.redirect_to_bi_connector, name='bi_connector'),
#     path('products/budget_sale_dashboard/',  views.sales_dashboard, name='pages/sales_dashboard'),

# path('dashboardform/', views.dashboard_form, name='dashboardForm'),
#     path('team/', views.team, name='team'),
# path('appstore/', views.odoo_app_store, name='app_store'),
# path('products/skucast/', views.skucast, name='skucast'),

]
handler404 = 'pages.views.error_404_view'