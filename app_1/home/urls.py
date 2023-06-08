from django.urls import path
from .views import index_page, Telefons, register,login

app_name = 'home'

urlpatterns = [
    path('', index_page, name='index_page'),
    path('Price/<int:top>', Telefons, name='Products'),
    path('register/', register, name='register'),
    path('login/', login, name='login')

    # path('Brands/', Brands, name='Brands'),
    # path('Product/', Product, name='Telefon')
    #
]
