from django.contrib import admin
from django.urls import path, include
from .views import register, login, log_out, account
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', log_out, name='logout'),
    path('account/', account, name='user-account'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="users/password-reset.html"), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="users/password-sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password-form.html"), name="password_reset_confirm"),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="users/password-complete.html"), name="password_reset_complete"),



]