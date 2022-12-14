from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('our_services', views.our_services, name='our_services'),
    path('faq', views.faq, name='faq'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('interior', views.interior, name='interior'),
    path('showroom', views.showroom, name='showroom'),
    path('blog', views.blog, name='blog'),
]
