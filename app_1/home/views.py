from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Telefon, Brand, Product, Users

def index_page(request):
    return render(request, "index.html")

def Telefons(request, top):
    queryset = Product.objects.all().order_by('-price')[:top]
    # print(queryset[0].price)
    return render(request, "max_price.html", {'products': queryset})


def register(request):
    if request.POST:
        data = request.POST.dict()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        number = data.get('number')
        country = data.get('country')
        user = Users(name=name, email=email, password=password, phone_number=number, country=country)
        user.save()
        return HttpResponse('succes')
        # return redirect("home:login")
    return render(request, 'register.html')

def login(request):
    if request.POST:
        data = request.POST.dict()
        email = data.get('email')
        password = data.get('password')
        user = Users.objects.filter(email=email, password=password)
        print(user)
        if user:
            return redirect("home:Products", top=9)
        else:
            return HttpResponse("Xatolik")
    return render(request, 'login.html')
