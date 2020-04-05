"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views # Inbuilt 
from django.urls import path, include  # Main app> create urls.py> copy entire urls.py of this page paste> and create paths 

# from appName import views as appName_views to avoid confusion we can use views instead of appName_views
from users import views as users_views

#copied from django doccumentation for profile image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # Home page 

    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name = 'password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name = 'password_reset_done'),
    
    path('profile/', users_views.profile, name = 'profile'),
    path('register/', users_views.register, name = 'register'),
]

# To avoid viewers interfere
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
