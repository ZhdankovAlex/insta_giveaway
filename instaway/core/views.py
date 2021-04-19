from django.shortcuts import render, redirect
from django.http import *
from instabot import *
from .forms import *

def index(request):
    if request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            url = postForm.cleaned_data["url"]
            comment = postForm.cleaned_data["comment"]
            author = postForm.cleaned_data["author"]
            like = postForm.cleaned_data["like"]
            hashtag = postForm.cleaned_data["hashtag"]
            data = {"url": url,
                    "comment": comment,
                    "author": author,
                    "like": like,
                    "hashtag": hashtag}
            # запускаем работу с instabot
            bot = Bot()
            # здесь указываем логин и пароль от НАШЕГО аккаунта insta
            INST_USERNAME = "zamada.kz"
            INST_PASSWORD = "Zamada2021$"
            bot.login(username = INST_USERNAME,  password = INST_PASSWORD)
            user_id = bot.get_user_id_from_username("lego")
            user_info = bot.get_user_info(user_id)
            data["user_info"] = user_info['biography']
            #media_link = url
            #media_pk = bot.get_media_id_from_link(media_link)
            # здесь будем хранить итоговый список
            #result = []
            # получаем список лайкнувших
            #if (like): # по умолчанию имеем неизменяемый флаг True
            #    users_liked = bot.get_media_likers(media_pk)
            #    result.append(users_liked)
            # получаем список всех комментариев
            #if (comment):
            #    all_comments = bot.get_media_comments_all(media_pk)
            #    result.append(all_comments)
            # получаем список авторов
            #elif (author):
            #    all_comments = bot.get_media_comments_all(media_pk)
            #    authors = list(set(all_comments))
            #    result.append(authors)
            # получаем список хэштегов
            #----------------------------------------------
            #data["result"] = result
            return render(request, "result.html", context=data)
        else:
            return HttpResponse("Неверные входные данные")
    else:
        postForm = PostForm()
        return render(request, "index.html", {"form": postForm})
