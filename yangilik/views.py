from django.shortcuts import render
from .models import Yangilik,Categoriy
# Create your views here.

def home (request):
    category = Categoriy.objects.all().order_by('id')
    context = {'category':category}
    return render(request ,'home.html',context)

def get_yangiliklar(request,pk):
    yangilik = Yangilik.objects.filter(categoy__id=pk)  #.order_by('-id')
    context = {'yangilik':yangilik}
    return render(request,'yangilik.html',context)

def get_yangilik(request,pk):
    yangilik = Yangilik.objects.filter(pk=pk)
    contex = {'yangilik':yangilik}
    return  render(request,'yangilik_ful.html',contex)


