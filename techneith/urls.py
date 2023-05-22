from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('service/', include('service.urls')),
    path('', include('payments.urls')),
    path('products/', include('products.urls')),
    path('froala_editor/', include('froala_editor.urls'))
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'pages.views.error_404'
