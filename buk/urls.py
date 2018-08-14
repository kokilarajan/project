from django.conf.urls import url
from django.contrib import admin
from buk.views import AddBuk,listbook,Editbuk,ByView,Adminhome

from django.conf import  settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from buk import views





urlpatterns = [
   
    # url(r'^book/catgr/',Addcateg.as_view(),name='book_cat'),
    url(r'^book/ad/',AddBuk.as_view(),name='book_add'),
    # url(r'^all/c/',listcat.as_view(),name='al_cat'),
    url(r'^all/book/',listbook.as_view(),name='al_buk'),
    # url(r'^edit/(?P<pk>[0-9]+)/$',Editcatg.as_view(),name='edit_cat'),

    
    url(r'^editbukz/(?P<pk>[0-9]+)/$',Editbuk.as_view(),name='edit_buk'),
    url(r'^buy/(?P<pk>[0-9]+)/$',ByView.as_view(),name='buy_buk'),
    
    # url(r'^buynow/(?P<pk>[0-9]+)/$',BuynowView.as_view(),name='by_nw'),
    ]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 