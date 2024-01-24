from django.shortcuts import render

def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    user_name = request.POST.get("user_name", "")
    user_pwd = request.POST.get("user_pwd", "")
    
    

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