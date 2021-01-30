"""booking URL Configuration

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
from django.contrib import admin
from django.urls import path
from authentication import views as views_auth
from book import views as views_book


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_book.index_view),
    path('login/', views_auth.login_view), 
    path('logout/',views_auth.logout_view),
    path('register/', views_auth.register), 
    path('booking/', views_book.booking_view),
    path('booking_list',views_book.booking_list), 
    path('booking/delete/<int:pk>',views_book.delete_booking), 
]
