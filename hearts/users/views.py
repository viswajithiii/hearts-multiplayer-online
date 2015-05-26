from django.shortcuts import render, render_to_response, redirect
from users.forms import AddUserForm, UserLoginForm
from django.template.context import RequestContext
from django.contrib.auth.models import User
from users.models import userprofile
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def register_user(request):

    add_user_form = AddUserForm()
    if request.method == "POST":
        add_user_form = AddUserForm(request.POST)
        if add_user_form.is_valid():
            new_user = User.objects.create_user(
                username = add_user_form.cleaned_data['username'],
                password = add_user_form.cleaned_data['password'],
                first_name = add_user_form.cleaned_data['first_name'],
                last_name = add_user_form.cleaned_data['last_name'],
                )    
            profile = userprofile.objects.create(user=new_user)
            new_user.save()
            profile.save()
            return redirect('users.views.login')
        else:
            return render_to_response('register.html', locals(), context_instance = RequestContext(request))
    else:
        return render_to_response('register.html', locals(), context_instance = RequestContext(request))

def login(request):
    if request.user.is_authenticated():
        return redirect('users.views.home')
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username = login_form.cleaned_data['username'],password=login_form.cleaned_data['password'])
            if user is not None: #Login successful
                auth_login(request,user)
                return redirect('users.views.home')
            else:
                login_error = True
                return render_to_response('login.html',locals(),context_instance = RequestContext(request))
        else:
            login_error = True
            return render_to_response('login.html',locals(),context_instance = RequestContext(request))
    else:
        login_form = UserLoginForm()
    return render_to_response('login.html',locals(),context_instance = RequestContext(request))

def home(request):
    authenticated = request.user.is_authenticated()
    return render_to_response('index.html',locals(),context_instance = RequestContext(request))

def logout(request):
    auth_logout(request)
    return redirect('users.views.home')
