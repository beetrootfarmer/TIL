from dataclasses import fields
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    # ArticleForm Class 가 어떻게 정의되는지 
    # 그 정보는 Meta class에 넣는다 
    class Meta:
        model = Article
        # fields = "__all__"
        exclude = ('user',)
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article',)