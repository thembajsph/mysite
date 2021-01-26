from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
# we use index for the main page of our app

#  whenever there is a request to /products call this index function , we need to map it
#  map this url to this function(address)

def index(request):
    products = Product.objects.all()
    # return HttpResponse("Hello World")
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('New Products')