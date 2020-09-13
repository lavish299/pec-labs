from django.shortcuts import render
from django.http import HttpResponse
from home.models import Equipment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    db=Equipment.objects.values()
    context={'products': db}
    return render(request,'home/home.html',context)

class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'home/product_detail.html'