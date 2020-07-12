from bmr import views
from django.conf.urls import url
urlpatterns=[
    url('viewbooks',views.viewbooks),
    url('editbook',views.editbook),
    url('searchbook', views.searchbook),
    url('search', views.search),
    url('edit', views.edit),
    url('deletebook', views.deletebook),
    url('newbooks', views.NEWBOOK),
    url('concatinate', views.add),
    url('login', views.userlogin),
    url('logout', views.userlogout),

   url('download', views.download),



]
