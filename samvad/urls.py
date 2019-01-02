"""samvad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from basicapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.user_login, name='login'),
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('basicapp/', include('basicapp.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('superAdmin/', views.superAdmin, name='superAdmin'),
    path('instituteAdmin/', views.instituteAdmin, name='instituteAdmin'),
    path('register/', views.superAdmin, name='registerInstituteAdmin'),
    path('instituteAdmin/adduser/', views.addUser, name='adduser'),
    path('index/addNewsFeed/', views.index, name='addnewsfeed'),
    path('index/<int:pk>/', views.NewsFeedDetail.as_view(),name ='detail'),
    path('accountInfo/', views.userAccountInfo, name='accountInfo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
