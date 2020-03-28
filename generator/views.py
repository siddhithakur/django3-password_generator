from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    #return HttpResponse("hi")
    return render(request,'generator/home.html')
def password(request):
    #return HttpResponse("hi")
    chars=list("abcdefghijklmnopqrstuvwxyz")
    thepassword=""

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        chars.extend(list('@#$%^&*('))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))

    length=int(request.GET.get('length',2))
    for i in range(length):
        thepassword+=random.choice(chars)

    return render(request,'generator/password.html',{'password':thepassword})

def new_page(request):
    return render(request,'generator/new_page.html')

