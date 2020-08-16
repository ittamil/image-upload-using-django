from django.shortcuts import render, redirect
from app.forms import Imageform
# Create your views here.
def index(request,*args, **kwargs):
    if request.method == "POST":
        form = Imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Imageform()        

    
    return render(request,'index.html',{'form':form})