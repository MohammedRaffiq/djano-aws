"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1 import views as v1
from django.contrib.auth import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.home, name='home'),
    path('owner/<int:pk>/', v1.owner, name='owner'),
    path('create/', v1.create, name='create'),
    path('update/<int:pk>/', v1.update, name='update'),
    path('delete/<int:pk>/', v1.delete, name='delete'),
    path('login/',views.LoginView.as_view(template_name='app1/login.html'), name='login'),
    path('logout/',views.LogoutView.as_view(template_name='app1/logout.html'), name='logout'),
    path('register/',v1.Register, name='register'),
    path('deletemessage/<int:pk>/', v1.deletemessage, name='deletemessage'),
    path('profile_details/', v1.profile_details, name='profile_details'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

