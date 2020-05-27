from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    #path(r'', views.upload),
    #path('/documents/', views.doclist),

    #path('documents/upload', views.upload_doc, name='Document upload'),

]

# Serving media on the local machine
# Shouldn't be used in productive environments
# settings is only in debug mode within the development
# Setting the path for the uploaded media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)