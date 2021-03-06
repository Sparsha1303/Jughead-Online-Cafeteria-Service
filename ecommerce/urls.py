"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.views.generic import TemplateView
from accounts.views import login_page,register,guest_login_view
from carts.views import (
        udupi_detail_cart_api_view,
        tango_detail_cart_api_view,
        munch_detail_cart_api_view)
from .views import home,about,contact
from billing.views import payment_method_view,payment_method_createview

urlpatterns = [

    url(r'^$',home,name='home'),
    url(r'^about/$',about,name='about'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^login/$',login_page,name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    url(r'^register/guest/$',guest_login_view,name='guest_register'),
    url(r'^register/$',register,name='register'),
    url(r'^bootstrap/$',TemplateView.as_view(template_name = 'bootstrap/example.html') ),
    url(r'^cafeterias/',include("products.urls", namespace = 'cafeterias')),
    url(r'^search/',include("search.urls", namespace='search')),
    url(r'^carts/',include("carts.urls", namespace = 'carts')), 
    url(r'^api/cart/$',udupi_detail_cart_api_view,name='udupi_detail_cart_api_view_created'),
    url(r'^billing/payment-method/create/$',payment_method_createview,name='billing-payment-method-endpoint'),
    url(r'^billing/payment-method/$',payment_method_view,name='billing-payment-method'),
    url(r'^api/cart/$',tango_detail_cart_api_view,name='tango_detail_cart_api_view_created'),
    url(r'^api/cart/$',munch_detail_cart_api_view,name='munch_detail_cart_api_view_created'),
    path('admin/', admin.site.urls),
]
                                                                      
if settings.DEBUG:

    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
