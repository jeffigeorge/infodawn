from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from master.models import Vehicle, Accessories
from master.forms import Vehicleform, Accessoriesform
from user.models import Service, Breakdown, Feedback


# Create your views here.
class Homeview(TemplateView):
    template_name = 'home.html'


class Masterhomeview(TemplateView):
    template_name = 'masterhome.html'


class Addvehicleview(CreateView):
    template_name = 'masterav.html'
    model = Vehicle
    form_class = Vehicleform
    success_url = '/master/masterhome'


class Listvehicleview(ListView):
    template_name = 'masterlv.html'
    model = Vehicle
    context_object_name = 'list'


class Upvehicleview(UpdateView):
    template_name = 'masterav.html'
    model = Vehicle
    fields = ['Vehicle_Name', 'Vehicle_Type', 'Description', 'Vehicle_Color', 'Rate', 'Weight', 'Capacity',
              'Mileage', 'Fuel', 'Vehicle_Model', 'Year_of_built', 'Autogear', 'Seatcap', 'Center_lock',
              'Power_steering', 'Power_break', 'Tyre', 'Chassis', 'Vehicle_Image']
    success_url = '/master/listvehicle'


class Devehicleview(DeleteView):
    template_name = 'delbtn.html'
    model = Vehicle
    success_url = '/master/listvehicle'


class Addaccview(CreateView):
    template_name = 'masteraa.html'
    model = Accessories
    form_class = Accessoriesform
    success_url = '/master/masterhome'


class Listaccview(ListView):
    template_name = 'masterla.html'
    model = Accessories
    context_object_name = 'list'


class Upaccview(UpdateView):
    template_name = 'masteraa.html'
    model = Accessories
    fields = ['Accessory_Name', 'Vehicle_Name', 'Description', 'Rate', 'Accessory_Image']
    success_url = '/master/listacc'


class Deaccview(DeleteView):
    template_name = 'delbtn.html'
    model = Accessories
    success_url = '/master/listacc'


class Serviceview(ListView):
    template_name = 'masterservice.html'
    model = Service
    context_object_name = 'list'


class Breakdownview(ListView):
    template_name = 'masterbreakdown.html'
    model = Breakdown
    context_object_name = 'list'

class Listfeedbackview(ListView):
    template_name = 'mvieweedback.html'
    model = Feedback
    context_object_name = 'list'

class LReply(UpdateView):
    template_name = 'reply.html'
    model = Breakdown
    fields = ['Reply', ]
    success_url = '/master/masterhome'

class SReply(UpdateView):
    template_name = 'reply.html'
    model = Service
    fields = ['Reply', ]
    success_url = '/master/masterhome'
