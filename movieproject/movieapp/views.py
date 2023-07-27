from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import MovieForm
from movieapp.models import Movie


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movies':movie
    }
    return render(request,'index.html',context)

def details(request,mov_id):
    movie=Movie.objects.get(id=mov_id)
    return render(request,"details.html",{'movie':movie})


def add_movie(request):
    print("here")
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        yr = request.POST['yr']
        img = request.FILES['img']
        movie=Movie(name=name,desc=desc,yr=yr,img=img)
        movie.save()
        messages.info(request, "Data saved")
        return render(request,"add.html")

    else:
        messages.info(request, "Data not saved")

    return render(request, "add.html")


def update(request,mov_id):
    movie=Movie.objects.get(id=mov_id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        messages.info(request, "Data updated")
        return  redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,mov_id):
    if request.method=='POST':
        movie=Movie.objects.get(id=mov_id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')