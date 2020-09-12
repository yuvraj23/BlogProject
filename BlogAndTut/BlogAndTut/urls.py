"""BlogAndTut URL Configuration

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
from django.urls import path,include,re_path
from BlogApp import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/heyim/imcodehoolic/normal_user_not_allow/donttrythisagian/', admin.site.urls),
    path('',views.home,name="home"),
    path('allProblem/',views.problemSet,name="allProblem"),
    path('allBlog/',views.BlogSet,name="allBlog"),
    path('PrivacyPolicy/',views.PrivacyPolicy,name="PrivacyPolicy"),
    path('TermsAndConditions/',views.TermsAndConditions,name="TermsAndConditions"),
    re_path('viewProfile/(?P<id>\d+)/',views.ViewProfile,name="viewProfile"),
    path('allJob/',views.JobSet,name="allJob"),
    path('about/',views.about,name="about"),
    path('signup/',views.signup_view,name="signup"),
    re_path('offcampus/(?P<id>\d+)/',views.OffCampusDrive, name='offcampus'),
    re_path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/(?P<lk>[^/]+)/(?P<dis>[^/]+)/$',
    views.dashboard,name='dashboard_url'),
    path('ProblemSubmission/',views.Coding_Request,name="ProblemSubmission"),
    re_path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/(?P<lk>[^/]+)/(?P<dis>[^/]+)/(?P<ps>[^/]+)/$',
    views.ShowProblemStatement,name="viewAllProbelms"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
