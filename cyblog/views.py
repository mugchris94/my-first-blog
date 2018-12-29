from django.shortcuts import render,redirect
import datetime
from django.utils import timezone
from cyblog.models import Post
from . import forms
from cyblog.forms import Create_Post,SearchForm,Create_User,UserLoginForm
from django.contrib.auth import (
    
    authenticate,
    login,
    logout
)


# Create your views here.

def login_view(request):
    form= UserLoginForm(request.POST)
    if form.is_valid():
        username= form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        
        user=authenticate(username=username,password=password)
        login(request,user)

        redirect('post_list')

    context={

        'form':form
    }
    form= UserLoginForm()
    return render(request,'cyblog/login.html',context)

def logout_view(request):
    logout(request)
    return render(request,'cyblog/post_list.html')

def post_list(request):
    view_date= datetime.datetime.now().date()
    posts_to_date= Post.objects.filter(created_date__lte= timezone.now()).order_by('created_date')
    context= {
        'view_date':view_date,
        'posts_to_date':posts_to_date

    }
    return render(request,'cyblog/post_list.html',context)
def create_post(request):
    form = Create_Post()
    if request.method == "POST":
        form = Create_Post(request.POST)
        if form.is_valid():
           post= form.save(commit=False)
           post.author= request.user
           post.created_date= timezone.now()
           post.save()

           return redirect('create_user')
    else:
         form= Create_Post()
    return render(request,'cyblog/create_user.html',{'form':form})

    context= {
                'form':form
    }
    return render(request,'cyblog/create_user.html',context)

def search_post(request):
    if request.method == "POST":
        Myform = SearchForm(request.POST)
        if Myform.is_valid():
            error = 'false'
            titles = Myform.cleaned_data['title']
            db_title= Post.objects.filter(title=titles)
            args = {
                'form' : Myform,
                'titles' : db_title,
                'error' : error
                }
            return render(request,'cyblog/search_post.html',args)

    else:
          Myform = SearchForm()
    return render(request,'cyblog/post_list.html',{'form':Myform})



def create_user(request):
    if request.method == 'POST':
        New_Form= Create_User(request.POST)
        if New_Form.is_valid():
            emails= New_Form.cleaned_data['email']
            passrwd= New_From.cleaned_data['username']
            passrwd_conf= New_From.cleaned_data['password_confirm']
            args={
            'email':emails

            }
            redirect('post_list')
    else:
        New_Form= Create_User()
    context={
    'form':New_Form,
    }
    return render(request,'cyblog/create_user.html',context)
