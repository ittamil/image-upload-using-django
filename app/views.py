from django.shortcuts import render, redirect
from app.forms import Imageform
from app.models import Image

def index(request,*args, **kwargs):
    image = Image.objects
    if request.method == "POST":
        form = Imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Imageform()   
    context = {
        'form':form,
        'image':image
    }         
    return render(request,'index.html',context)
