from django import forms

class PostForm(forms.Form):
    # поле ввода url поста из instagram
    url = forms.URLField(label="Ссылка на пост")
    # чекбокс комментариев (учитываем все комментраии от каждого человека)
    comment = forms.BooleanField(label="Выбрать победителя из комментариев",
                                 help_text="учитываем все комментарии от каждого пользователя",
                                 required=False)
    # чекбокс авторов (учитываем по одному комментарию от одного человека)
    author = forms.BooleanField(label="Выбрать победителя из авторов",
                                help_text="учитываем один комментарий от пользователя",
                                required=False)
    # чекбокс лайков
    like = forms.BooleanField(label="Выбрать победителя из лайков",
                              required=False)
    # чекбокс хэштегов (учитваем первый хэштег в описании поста)
    hashtag = forms.BooleanField(label="Выбрать победителя из хэштегов",
                                 help_text="ищем по первому хэштегу из описания поста",
                                 required=False)
    # порядок полей
    field_order = ["url", "comment", "author", "like", "hashtag"]
