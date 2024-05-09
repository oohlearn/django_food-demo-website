from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
# django有內建使用者驗證相關表格
from .forms import RegisterForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created!')
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return render(request, "users/logout.html")


def index(request):
    return render(request, "users/index.html")

@login_required
def profile_page(request):
    return render(request, "users/profile.html")
