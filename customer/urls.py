from django.conf.urls import url
from django.contrib import admin

from django.conf import  settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.contrib import auth



from customer.views import HomeView,BookView,AboutView,ContactView,SpecialView,RegisterView
from customer import views

urlpatterns = [
   
    url(r'^home/',views.HomeView,name='home'),
    url(r'^aboutus/',BookView.as_view(),name='Categ'),
    url(r'^books/',AboutView.as_view(),name='abt'),
    url(r'^contact/',ContactView.as_view(),name='cnct'),
    url(r'^best/',SpecialView.as_view(),name='best'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^regist/',RegisterView.as_view(),name='register'),
    url(r'^adminhome/',views.AdminHome,name='adminhome'),

   
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_URL)