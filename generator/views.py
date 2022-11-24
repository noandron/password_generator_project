from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    
    charachters = list(string.ascii_lowercase)
    special_symbols = ['~','!','@','#','$','%','^','&','*']
    int_nums = [str(k) for k  in range(10)]

    # берет из home.html поля select параметр с name = 'length'
    # 12 - значение по умолчанию
    length  = int(request.GET.get('length', 12)) 
    thepassword = ''
    upcase = request.GET.get('uppercase')
    nums = request.GET.get('numbers')
    spec = request.GET.get('special')
 
    if nums == 'on': 
        charachters.extend(int_nums)
    if spec == 'on':
        charachters.extend(list(special_symbols)) 
    if upcase == 'on':
        charachters.extend(list(string.ascii_uppercase))

    for i in range(length):
        thepassword += random.choice(charachters)
    
    return render(request, 'generator/password.html', {'password':thepassword})