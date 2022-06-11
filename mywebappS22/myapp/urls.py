from django.urls import path
from myapp import views
#by Allen
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.render_index, name='index0.html'),
    path('about', views.about),
    path('photogallery', views.photogallery),
    path('myaccount', views.myaccount),
    path('register', views.register),
    path('attraction', views.attraction),
    path('ambassador', views.ambassador),
    path('sports', views.sports),
    path('home', views.home),
]

#by Allen
urlpatterns += staticfiles_urlpatterns()