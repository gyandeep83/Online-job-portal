"""
URL configuration for online_job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('signup/', views.signup_view,name="signup_view"),
    path('login/', views.login,name="login"),
    path('homepage/', views.homepage, name="homepage"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),
    path('reset/<uidb64>/<token>/', views.reset_password_confirm, name='password_reset_confirm'),
    path('companies/', views.company_list, name='company_list'),
    path('jobs/', views.all_jobs, name='all_jobs'),
    path('feedback/', views.feedback_view, name="Feedback"),
    path('jobapplication/<int:desc_id>/', views.apply_job, name='jobapplication'),
    path('thankyou/', views.thank_you_page, name='thank_you_page'),
    path('companydetails/<int:company_id>/', views.company_details, name='company_details'),
    path('contact/', views.contact_details, name='contact_details'),
    path('success/', views.success, name='success'),


]
