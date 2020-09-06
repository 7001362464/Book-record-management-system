from brm import views
from django.conf.urls import url
urlpatterns=[
    url('view_books',views.view_books),
    url('edit_book',views.edit_book),
    url('search_book', views.search_book),
    url('search', views.search),
    url('edit', views.edit),
    url('del_book', views.del_book),
    url('new_book', views.new_book),

    url('add1', views.add),
    url('login',views.userlogin),
url('logout',views.userlogout),



