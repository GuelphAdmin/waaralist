from django.shortcuts import redirect, render
from members.models import memberdetails
from django.contrib.auth import authenticate, login as dj_login,  logout
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
        tasks = memberdetails.objects.filter(is_completed=False).order_by('created_at')[:10]
        complete = memberdetails.objects.filter(is_completed=True).order_by('updated_at')
        context = {
                        'dictTask':tasks,
                        'dictcomp':complete,
                }

        return render(request, 'home.html',context) 
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                dj_login(request, user)
                #success page
                print("Login Successful")
                tasks = memberdetails.objects.filter(is_completed=False).order_by('created_at')
                complete = memberdetails.objects.filter(is_completed=True).order_by('updated_at')
                context = {
                        'dictTask':tasks,
                        'dictcomp':complete,
                        }
                return render(request, 'home.html',context) 
    else :
                print("bad login")
                messages.success(request,'Invalid UserName or Password')
    return render(request, 'loginmain.html')