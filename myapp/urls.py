from django.urls import path

from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('image', views.addImage, name="image"),
    path('contact',views.contact,name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)