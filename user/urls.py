from django.urls import path, include
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='password_change_form.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='password_reset_form.html',
        email_template_name='password_reset_email.html',
        success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url=reverse_lazy('user:login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),

]
