from django.shortcuts import render, redirect
from django.http import *
from instabot import Bot

def index(request):
    return render(request, "index.html")

def main(request):

    username = request.GET.get("name", "Undefined user")
    profile_icon = request.GET.get("avatar", "user.jpg")
    data = {"profile_icon": profile_icon, "username": username}
    return render(request, "main.html", context=data)

# статусные коды
def m304(request):
    return HttpResponseNotModified()

def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")

def m403(request):
    return HttpResponseForbidden("<h2>Forbidden</h2>")

def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")

def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")

def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")

def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")
