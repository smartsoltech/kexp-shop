
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductDetailView


urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contacts', views.contacts, name="contacts"),
    path('item/<int:pk>', views.ProductDetailView.as_view(), name="iteminfo")
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)