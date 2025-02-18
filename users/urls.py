from django.urls import path
from users.views import inicio, about_view, home_view
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)

urlpatterns = [
    path('', LoginView.as_view(
        template_name="base.html"
    ),
         name='login'
         ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('about/', about_view, name='about'),
    path('home/', home_view, name='home'),
]