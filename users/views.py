from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    print("Inicio")
    return HttpResponse("<h1>Hola Ahora si</h1>")

def second_view(request):
    print("second view")
    context = {
        "name": "Luis",
        "second_name": "Rios",
        "age": 48,
    }
    return render(request, "base.html", context=context)
