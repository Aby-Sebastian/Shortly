from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    # user login, logout and register
    path('register/',views.registerUser,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),

    # password change
    path('change_password/', 
        auth_views.PasswordChangeView.as_view(template_name='password/change_password.html'), 
        name="change_password"),
    path('password_change_done/', 
        auth_views.PasswordChangeDoneView.as_view(template_name='password/password_change_done.html'), 
        name="password_change_done"),

    # password reset 
    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'), 
        name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_sent.html'), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>', 
        auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_form.html'), 
        name='password_reset_confirm'),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_done.html'), 
        name='password_reset_complete'),

]
