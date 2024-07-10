"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views 



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.mainpage, name="main"),
    path('<slug:slug_>', views.itempage, name='item'),
    path("shoes/", views.shoespage, name="shoes"),
    path('api/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('api/get-items/', views.get_data, name='get_data'),
    path("collection/", views.collectionpage, name="collection"),
    path("categories/", views.categories, name="categories"),
    path("contact/", views.contact, name="contact"),
    path("account/", include("account.urls"), name="account"),



    path("account", include("account.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
