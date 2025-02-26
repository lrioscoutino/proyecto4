from django.urls import path
from users.views import (
    inicio,
    about_view,
    home_view,
    third_view,
    customer_view,
    edit_customer_view,
    delete_customer_view,
)
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
    path('third/', third_view, name='third'),
    path('customer/', customer_view, name='customer'),
    path('customer/edit/<int:pk>/', edit_customer_view, name='edit_customer'),
    path('customer/delete/<int:pk>/', delete_customer_view, name='delete_customer'),
]
