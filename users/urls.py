from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name="users"

urlpatterns = [

    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('password/reset', PasswordResetView.as_view(template_name="users/password_reset.html"), name="reset-pass"),
    path('password/reset/done', PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="reset-pass-done"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="reset-pass-confirm"),
    path('password/reset/updated/', PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="reset-comp"),
    path('profile', views.userprofile, name="profile")
]