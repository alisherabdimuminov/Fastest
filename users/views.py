from django.http import HttpRequest
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


def login_(request: HttpRequest):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request=request, user=user)
            return redirect("home")
        else:
            context["errors"] = "Ma'lumotlar noto'g'ri"
    return render(
        request=request,
        template_name="login.html",
        context=context
    )

def logout_(request: HttpRequest):
    logout(request=request)
    return redirect("login")