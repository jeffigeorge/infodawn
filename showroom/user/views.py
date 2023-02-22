from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, FormView, View, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from user.models import Userdetails, Service, Breakdown, Feedback
from user.forms import Registrationform, UserForm, LoginForm, Serviceform, Breakdownform, Feedbackform
from master.models import Vehicle, Accessories
import razorpay
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class Userhomeview(TemplateView):
    template_name = 'uhome.html'


class Registrationview(FormView):
    template_name = 'reg.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        self.object = None

        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        cust_form = Registrationform()
        return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))

    def post(self, request, *args, **kwargs):
        self.object = None

        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        cust_form = Registrationform(self.request.POST)
        if (user_form.is_valid() and cust_form.is_valid()):
            return self.form_valid(user_form, cust_form)
        else:
            return self.form_invalid(user_form, cust_form)

    def form_valid(self, user_form, cust_form):
        self.object = user_form.save()  # User model save

        self.object.is_staff = True  # edit user object
        self.object.save()
        cust_obj = cust_form.save(commit=False)  # Customer Model save(contact,address,place)
        cust_obj.basic_data = self.object  # saving OneToOnefield ,edit cust_obj
        cust_obj.save()
        return super(Registrationview, self).form_valid(user_form)

    def form_invalid(self, user_form, cust_form):
        return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))

    def get_success_url(self, **kwargs):
        return ('/user/login/')


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # print(request.user)

            try:
                user_obj = User.objects.get(username=request.user)
                cust = Userdetails.objects.get(basic_data=user_obj)

            except:
                user_obj = None
                cust = None

            if request.user.is_superuser:
                return redirect('/master/masterhome')
            else:
                return redirect('/user/userhome')
        else:
            return redirect('/user/login')


class VehicleView(ListView):
    template_name = 'uvehicle.html'
    model = Vehicle
    context_object_name = 'list'


class VehicledetailsView(DetailView):
    template_name = 'uvehicledetails.html'
    model = Vehicle


def payment(request):
    if request.method == "POST":
        name = request.POST.get('username')
        amount = 500

        client = razorpay.Client(
            auth=("rzp_test_rYcuWKCygjkElZ", "zTxPVsOVV2k9AGxlpTikUeBg"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

    return render(request, 'payment.html')


@csrf_exempt
def success(request):
    return render(request, "success1.html")


class Buy(DetailView):
    model = Vehicle
    template_name = 'payment.html'


class AccessoriesView(ListView):
    template_name = 'uacc.html'
    model = Accessories
    context_object_name = 'list'


class AccessoriesdetailsView(DetailView):
    template_name = 'uaccdetails.html'
    model = Accessories


class Buy1(DetailView):
    model = Accessories
    template_name = 'payment1.html'


class Serviceview(CreateView):
    template_name = 'uservice.html'
    model = Service
    form_class = Serviceform
    success_url = '/user/userhome'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Serviceview, self).form_valid(form)


class Breakdownview(CreateView):
    template_name = 'ubreakdown.html'
    model = Breakdown
    form_class = Breakdownform
    success_url = '/user/userhome'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Breakdownview, self).form_valid(form)


class Feedbackview(CreateView):
    template_name = 'ufeedback.html'
    model = Feedback
    form_class = Feedbackform
    success_url = '/user/userhome/'


class Breakdownreportview(ListView):
    template_name = 'ubreakdownreport.html'

    def get(self, request):
        qs = Breakdown.objects.filter(user=request.user)
        context = {
            'list': qs
        }
        return render(request, self.template_name, context)


class Servicereportview(ListView):
    template_name = 'uservicereport.html'

    def get(self, request):
        qs = Service.objects.filter(user=request.user)
        context = {
            'list': qs
        }
        return render(request, self.template_name, context)
