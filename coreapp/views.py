from django.shortcuts import render, HttpResponseRedirect
from .forms import userforms, loginforms, add_post_forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import add_post
from django.contrib import messages

# Create your views here.

def us_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = loginforms(request=request, data= request.POST)
            if fm.is_valid():
                u_name = fm.cleaned_data['username']
                u_pass = fm.cleaned_data['password']
                user = authenticate(username= u_name, password= u_pass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/deshbord/')
            else:
                messages.warning(request,'You do not have such an account !')
                return HttpResponseRedirect('/')
        else:           
            fm = loginforms()
        return render(request, 'coreapp/login.html', {'fm':fm})
    else:
        return HttpResponseRedirect('/deshbord/')
    
def us_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        fm = userforms(request.POST)
        if fm.is_valid():
            messages.warning(request, 'Your Account Created Successfully !')
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = userforms()
    return render(request, 'coreapp/register.html', {'fm':fm})

def deshbord(request):
    if request.user.is_authenticated:
        print(request.user)
        post = add_post.objects.filter(user=request.user)
        print(post)
        return render(request, 'coreapp/deshbord.html',{'fm':post})
    else:
        return HttpResponseRedirect('/')

def search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            searched = request.POST['searched']
            fm = add_post.objects.filter(user=request.user,title__contains=searched)
            count_data = fm.count()
            return render(request,'coreapp/search.html',{'searched':searched,'fm':fm, 'count_data':count_data})
        else:
            return HttpResponseRedirect('/deshbord/')
    else:
        return HttpResponseRedirect('/')
        
def Postadd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = add_post_forms(request.POST)
            if fm.is_valid():
                post = fm.save(commit=False) # auto save off 
                post.user = request.user 
                post.save()
                messages.success(request, 'Your Post Created Successfully!!')
                return HttpResponseRedirect('/deshbord/')
        else:
            fm = add_post_forms() 
        return render(request,'coreapp/postadd.html',{'fm':fm}) 
    else:
        return HttpResponseRedirect('/')


def Postupdate(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = add_post.objects.get(pk=id)
            fm = add_post_forms(request.POST, instance=pi)
            if fm.is_valid():
                messages.success(request, 'Your Post Updated Successfully!!')
                fm.save()
                return HttpResponseRedirect('/deshbord/')
        else:
            pi = add_post.objects.get(pk=id)
            fm = add_post_forms(instance=pi)        
            return render(request, 'coreapp/update.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/')
    
    
def PostRemove(request,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = add_post.objects.get(pk=id)
            messages.warning(request, 'Your Post Deleted!!')
            pi.delete()
            return HttpResponseRedirect('/deshbord/')
        else:
            return render(request, 'coreapp/remove.html')
    else:
        return HttpResponseRedirect('/')