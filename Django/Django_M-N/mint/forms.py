from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = "__all__"
        exclude= ('user','like_users',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # field = '__all__'
        exclude = ('article',)