from django.shortcuts import render

def login(request):
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")

def vision_manage(request):
    return render(request,"vision_manage.html")

def vision_create(request):
    return render(request,"vision_create.html")

def okr(request):
    return render(request,"okr.html")

def milestone(request):
    return render(request,"milestone.html")

def schedule(request):
    return render(request,"schedule.html")