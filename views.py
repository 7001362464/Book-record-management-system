from django.shortcuts import render
from bmr.form import newbookform
from bmr import models
from django.shortcuts import redirect

import os
from django.conf import settings
from django.conf.urls import url

from django.http import HttpResponse
from bmr.form import searchform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='/bmr/login/')
def viewbooks(request):


    books=models.boi.objects.all();
    return render(request,'view_book.html',{'books':books})


def editbook(request):
    book=models.boi.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher,'pdf':book.pdf};
    form=newbookform(initial=fields);#it value and we pass the form with that value to edit
    return render(request,'edit_book.html',{'form':form,'book':book})
@login_required(login_url='/bmr/login/')


def searchbook(request):
    form=searchform();
    return render(request,'search_book.html',{'form':form})


def search(request):
    form=searchform(request.POST);
    books=models.boi.objects.filter(title=form.data['title'])#Basically use get() when you want to get a single unique object, and filter() when you want to get all objects that match your lookup parameters.
    res=render(request,'search_book.html',{'form':form,'books':books})
    return res;


def edit(request):
    if request.method=='POST':
        form=newbookform(request.POST)#it will take only the form values and put the value for each field of book class
        book = models.boi.objects.get(id=request.POST['bookid']);
        book.title=form.data['title'];
        book.price=form.data['price'];
        book.author=form.data['author']
        book.publisher=form.data['publisher'];
        book.pdf = request.FILES['pdf']
        book.save();
        books = models.boi.objects.all();
        return render(request, 'view_book.html', {'books': books})

def deletebook(request):
    bookid=request.GET['bookid'];
    book = models.boi.objects.get(id=bookid);
    book.delete();
    books = models.boi.objects.all();
    return render(request, 'view_book.html', {'books': books})





@login_required(login_url='/bmr/login/')  #it will check to the login and logout function if there has authentication or not
def NEWBOOK(request):
    form=newbookform()
    res=render(request,'new_book.html',{'form':form})
    return res;

def add(request):
    if request.method=='POST':
        '''form=newbookform(request.POST);
        book=models.boi();
        book.title=form.data['title'];
        book.price=form.data['price'];
        book.author=form.data['author'];
        book.publisher=form.data['publisher'];
        book.save();'''
        form= newbookform(request.POST, request.FILES)

        newdoc = models.boi(title=form.data['title'],price=form.data['price'],author=form.data['author'],publisher=form.data['publisher'],pdf=request.FILES['pdf'])
        newdoc.save()
        s="record stored<br><a href='bmr/viewbooks'>view books all</a>"
        return HttpResponse(s);


def userlogin(request):
    data={};
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password'];
        user=authenticate(request,username=username,password=password);
        if user:
            login(request,user);
            request.session['username']=username;  #it is handaled by session id every request has a session id.and this particular id is stored in server ram.and when again this session id request then for this particular id the value of request will come out and we can use it.

            books = models.boi.objects.all();
            return render(request, 'view_book.html', {'books': books})
        else:
            data['error']="Username or password not found"
            return render(request,"user_login.html",data);
    else:
        return render(request,"user_login.html",data);

def userlogout(request):
    logout(request);   #login() and logout() is for Restricting User to access pages without Login.by this login and logout django will understand whether user has login or logout before.
    return render(request, "user_login.html");


def download(request):

    return redirect('/media/{}'.format(request.GET.get('parameter')));

'''def download2(request):   #this is for download
    print(request.GET.get('parameter'))   #it is actually for download                     

    invoice_path = os.path.join(settings.MEDIA_ROOT, "{}").format(request.GET.get('parameter'))
    print(invoice_path)

    with open(invoice_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf') #for excel content_type='application/vnd.ms-excel'
            response['Content-Disposition'] = 'inline;filename=some_file.pdf'
            return response
    pdf.closed
    
    only it-> also we can use-->  return render(request, "download.html");   but you have to use url in html file from media and for audio play audio also'''



