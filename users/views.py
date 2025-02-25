from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from users.models import Customer

from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.decorators.vary import vary_on_headers

# Create your views here.
def inicio(request):
    print("Inicio")
    return HttpResponse("<h1>Hola Ahora si</h1>")

def second_view(request):
    context = {
        "name": "Luis",
        "second_name": "Rios",
        "age": 48,
    }
    return render(request, "base.html", context=context)

def third_view(request):
    if request.htmx:
        return render(request, "htmx.html")
    return render(request, "htmx.html")

def about_view(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers,
    }
    return render(request, "about.html", context=context)

def home_view(request):
    return render(request, "home.html")

def customer_view(request):
    if request.method == "POST":
        customer = Customer()
        customer.first_name = request.POST["first_name"]
        customer.last_name = request.POST["last_name"]
        customer.save()
        return redirect(reverse_lazy('about'))
    else:
        return render(request, "customer/form.html")

def edit_customer_view(request, pk):
    customer = Customer.objects.get(id=pk)
    context ={
        "customer": customer,
    }
    return render(request, "customer/form.html", context=context)
