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
from master.views import Homeview, Masterhomeview, Addvehicleview, Listvehicleview, Upvehicleview, Devehicleview, \
    Addaccview, Listaccview, Upaccview, Deaccview, Serviceview, Breakdownview, Listfeedbackview, LReply, SReply
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('home/', Homeview.as_view(), name='home'),
                  path('', Homeview.as_view(), name=''),
                  path('masterhome/', Masterhomeview.as_view(), name='masterhome'),
                  path('addvehicle/', Addvehicleview.as_view(), name='addvehicle'),
                  path('listvehicle/', Listvehicleview.as_view(), name='listvehicle'),
                  path('upvehicle/(?p<pk>[0-9]+)', Upvehicleview.as_view(), name='upvehicle'),
                  path('devehicle/(?p<pk>[0-9]+)', Devehicleview.as_view(), name='devehicle'),
                  path('addacc/', Addaccview.as_view(), name='addacc'),
                  path('listacc/', Listaccview.as_view(), name='listacc'),
                  path('upacc/(?p<pk>[0-9]+)', Upaccview.as_view(), name='upacc'),
                  path('deacc/(?p<pk>[0-9]+)', Deaccview.as_view(), name='deacc'),
                  path('logout/', auth_views.LogoutView.as_view(template_name="home.html"), name='logout'),
                  path('serviceview/', Serviceview.as_view(), name='serviceview'),
                  path('breakdownview/', Breakdownview.as_view(), name='breakdownview'),
                  path('listfeedback/', Listfeedbackview.as_view(), name='listfeedback'),
                  path('reply/(?p<pk>[0-9]+)', LReply.as_view(), name='reply'),
                  path('sreply/(?p<pk>[0-9]+)', SReply.as_view(), name='sreply'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
