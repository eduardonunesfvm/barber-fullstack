"""
URL configuration for page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    # 1. Página Inicial (Front-end)
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    # 2. Painel Administrativo
    path('admin/', admin.site.urls),

    # 3. Autenticação
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    # 4. Suas APIs (Back-end)
    path('api/appointments/', include('appointments.api.urls')),
    path('api/auth/', include('userauth.urls')),
    path('api/services/', include('services.api.urls')),
]




