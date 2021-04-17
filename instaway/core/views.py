from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import *
from instabot import Bot

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

# переадресация на главную страницу
def index(request):
    return render(request, 'insta/main.html')

# главная страница
def main(request):
    return render(request, 'insta/main.html')

# политика конфиденциальности
def privacy_policy(request):
    return render(request, 'insta/privacy_policy.html')

# авторизированный пользователь
@login_required
def authorized(request):
    return render(request, 'insta/authorized.html')

# страница админа (надо чекать админскую авторизацию,
# не должно быть возможности зайти простому смертному)
@login_required
def admin_page(request):
    return render(request, 'insta/admin_page.html')

# страничка с посчитанными лайками/репостами/хэштегами
@login_required
def link_parse(request):
    return render(request, 'insta/link_parse.html')

# результаты розыгрыша
@login_required
def results(request):
    return render(request, 'insta/results.html')

# прогрессбар
@login_required
def progress_bar(request):
    return render(request, 'insta/progress_bar.html')
