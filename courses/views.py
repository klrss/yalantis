from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.
from .models import Course
from .forms import CourseForm


def index(request):

    return render(request, "courses/index.html", {
        'courses': Course.objects.all()
    })


def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, "courses/detail.html", {
        "course": course
    })

def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    form = CourseForm(instance = course)
    if request.method=="POST":
        form=CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request, "courses/edit.html", {"form":form, "course":course})

def remove(request, course_id):
    course = Course.objects.filter(id=course_id).delete()
    if request.method == "POST":
        return HttpResponseRedirect(reverse("index"))
    return render(request, "courses/delete.html", {"course":course})


def add(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "courses/add.html", {"form": form})
    return render(request, "courses/add.html", {"form": CourseForm()})



