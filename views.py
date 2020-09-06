from django.shortcuts import render
from brm.forms import newbookform,searchform
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from brm import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/brm/login/')
def new_book(request):
    form=newbookform();
    res=render(request,'new_book.html',{'form':form})
    return res
@login_required(login_url='/brm/login/')
def add(request):
    if(request.method=="POST"):
        form=newbookform(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save();
    s="Record Stored<br><a href='/brm/view_books'>view books</a>";
    return HttpResponse(s);
@login_required(login_url='/brm/login/')
def view_books(request):
    books=models.Book.objects.all();
    res=render(request,'view_books.html',{'books':books})
    return res
@login_required(login_url='/brm/login/')
def edit_book(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'author':book.author,'publisher':book.publisher,'price':book.price}
    form=newbookform(initial=fields);
    res=render(request,'edit_book.html',{'form':form,'book':book})
    print(book.id)
    return res;
@login_required(login_url='/brm/login/')
def edit(request):
    if(request.method=='POST'):
        form=newbookform(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save();
    return HttpResponseRedirect("brm/view_books")
@login_required(login_url='/brm/login/')
def del_book(request):
    book = models.Book.objects.get(id=request.GET['bookid'])
    book.delete();
    return HttpResponseRedirect("brm/view_books")

@login_required(login_url='/brm/login/')
def new_book(request):
    form=newbookform();
    res=render(request,'new_book.html',{'form':form})
    return res
@login_required(login_url='/brm/login/')
def search_book(request):
    form=searchform()
    res=render(request,'search_book.html',{'form':form})
    return res
@login_required(login_url='/brm/login/')
def search(request):
    form = searchform(request.POST);
    books=models.Book.objects.filter(title=form.data['title']);
    res = render(request, 'search_book.html', {'form': form, 'books': books})
    return res;

def userlogin(request):
    data = {};
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'];

        user = authenticate(request, username=username, password=password);
        if user:
            login(request, user);
            request.session[
                'username'] = username;  # it is handaled by session id every request has a session id.and this particular id is stored in server ram.and when again this session id request then for this particular id the value of request will come out and we can use it.

            books = models.Book.objects.all();
            return render(request, 'view_books.html', {'books': books})
        else:
            data['error'] = "Username or password not found"
            return render(request, "user_login.html", data);
    else:
        return render(request, "user_login.html", data);
@login_required(login_url='/brm/login/')
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



