"""StudyManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from documents import views
from registration import views as registration_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('upload/', views.upload),

    # paths to the document sites
    path('documents/', views.doclist),
    path('documents/information_systems_development/', views.ISDdocs),
    path('documents/enterprise_architecture_management/', views.EAMdocs),
    path('documents/management_information_systems', views.MISdocs),
    path('documents/business_process_management/', views.BPMdocs),
    path('documents/data_and_application_security/', views.DASdocs),
    path('documents/data_management/', views.DMdocs),
    path('documents/business_statistics/', views.BSdocs),
    path('documents/innovation_lab/', views.ILdocs),
    path('documents/information_systems_modelling/', views.ISMdocs),
    path('documents/digital_innovation/', views.DIdocs),
    path('documents/data_science/', views.DSdocs),
    path('documents/digital_business/', views.DBdocs),
    path('documents/emerging_it_topics/', views.EITdocs),
    path('documents/human_centered_design/', views.HCDdocs),
    path('documents/research_methods/', views.RMdocs),
    path('documents/research_seminar/', views.RSdocs),
    path('documents/project_seminar/', views.PSdocs),
    path('documents/master_thesis/', views.MTdocs),


    #This path is needed, to delete the file (compares primary key of file)

    # This path is needed, to delete the file (compares primary key of file)
    path('documents/<int:pk>', views.deletedoc, name='deletedoc'),
   
    # include the auth app at accounts/ - standard provided by django
    path('registration/', registration_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

]
