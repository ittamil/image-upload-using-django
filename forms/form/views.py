from django.shortcuts import render, redirect
from form.forms import Imageform
# Create your views here.
def upload(request, *args, **kwargs):
    if request.method == 'POST':
        form = Imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Imageform()
    context = {
        'image':form
    }   
    return render(request,'index.html',context) 
 
    