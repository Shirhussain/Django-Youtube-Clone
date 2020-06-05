from django.urls import path
from django.contrib.auth import views as auth_views
from . views import register, channel


urlpatterns = [
    path('register/', register, name="register"),
    path('channel/', channel, name="channel"),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="user/password_reset.html"), name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"),name="password_reset_confirm"),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"),name="password_reset_complete"),
]






