from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainpage'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#For production, you'll want to serve your media files for something like Amazon CloudFront 