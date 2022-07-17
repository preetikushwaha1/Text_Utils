
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.



#=======Index function==============================#

def index_fun(request):
    return render(request, "index.html")

#====================Log IN function =================================#

def login_fun(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['pwd']

        user = auth.authenticate(username = username, password=pwd)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request, "invalid login")
            return redirect("login")
    else:
        return render(request,"login.html")


#====================Registration function =======================================#

def register_fun(request):
    if request.method == "POST":
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        usrname = request.POST['usrname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        confirm_pwd = request.POST['confirm_pwd']

        if(pwd == confirm_pwd):
            if(User.objects.filter(username=usrname).exists()):
                messages.info(request,"Username already exists")
                return redirect('register')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,"Email already exists")
                return redirect("register")
            else:
                user_login_details = User.objects.create_user(first_name=f_name, last_name = l_name, username=usrname,email =email, password=pwd)
                user_login_details.save()
                messages.info(request,"User created successfully")
                return redirect("login")
                
        else:
            
            messages.info(request,"password not matching")
        return redirect("register")
        
    else:
        return render(request,"register.html")


#==================logout function===============================#
def logout_fun(request):
    auth.logout(request)
    return redirect("/")


#===================Text Utils ============================#
def text_utils_func(request):
    return render(request, "Text_utils.html")





