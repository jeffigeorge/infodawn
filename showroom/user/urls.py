"""showroom URL Configuration

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

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user.views import Userhomeview, Registrationview, LoginView, VehicleView, VehicledetailsView, Buy, success, \
    AccessoriesView, AccessoriesdetailsView, Buy1, Serviceview, Breakdownview, Feedbackview, Breakdownreportview, Servicereportview
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('userhome/', Userhomeview.as_view(), name='userhome'),
                  path('reg/', Registrationview.as_view(), name='reg'),
                  path('login/', LoginView.as_view(), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name="home.html"), name='logout'),
                  path('vehicle/', VehicleView.as_view(), name='vehicle'),
                  path('vehicledetails/(?p<pk>[0-9]+)', VehicledetailsView.as_view(), name='vehicledetails'),
                  path('Buy/(?p<pk>[0-9]+)', Buy.as_view(), name='buy'),
                  path('Buy/success', success, name='Buy/success'),
                  path('accessories/', AccessoriesView.as_view(), name='accessories'),
                  path('accessoriesdetails/(?p<pk>[0-9]+)', AccessoriesdetailsView.as_view(),
                       name='accessoriesdetails'),
                  path('Buy1/(?p<pk>[0-9]+)', Buy1.as_view(), name='buy1'),
                  path('Buy1/success', success, name='Buy1/success'),
                  path('service/', Serviceview.as_view(), name='service'),
                  path('breakdown/', Breakdownview.as_view(), name='breakdown'),
                  path('breakdownreport/', Breakdownreportview.as_view(), name='breakdownreport'),
                  path('feedback/', Feedbackview.as_view(), name='feedback'),
                  path('servicereport/', Servicereportview.as_view(), name='servicereport'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
