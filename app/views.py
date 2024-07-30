from django.shortcuts import render
from .forms import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    ECFO=StuForm()
    return render(request,'login.html',{'ECFO':ECFO})