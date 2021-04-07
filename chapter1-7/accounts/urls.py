from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import CreateView

urlpatterns = [
    path('signup/', CreateView.as_view(
        template_name='accounts/signup.html',
        form_class=UserCreationForm,
        success_url='/',
    ), name='signup'),
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='accounts/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

