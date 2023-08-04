from django.shortcuts import render
from django.shortcuts import redirect
from products.models import Product
# Create your views here.
def index(request):
    context = {'products':Product.objects.all()}
    return render(request,"home/index.html",context)