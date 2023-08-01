
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
# Create your views here.
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)
        
        if not user_obj.exists():
            print("Accoount not exits")
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_email_verified:
            print("verify your account")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = email ,password = password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')
        
        
        print("Invalid Crendentials")
        return HttpResponseRedirect(request.path_info)
    
    return render(request,'accounts/login_page.html')




def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)
        
        if user_obj.exists():
            print("email already taken")
            return HttpResponseRedirect(request.path_info)
        
        
        user_obj = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email =email,
            username = email,
            
        )
        user_obj.set_password(password)
        user_obj.save()
        print("An email has been sent to email")
        return HttpResponseRedirect(request.path_info)
        
    return render(request,'accounts/signup.html')




def activate_email(request,email_token):
    try:
        user =  Profile.objects.get(email_token = email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')

    except Exception as e:
        return HTTPResponse("Invalid email token")