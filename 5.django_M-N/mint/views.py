from django.shortcuts import render, redirect
from mint.forms import ArticleForm, CommentForm
from mint.models import Article
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# from django.views.generic import ListView, DetailView,TemplateView



def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'mint/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # form.save_m2m()
            return redirect('mint:index')
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request, 'mint/create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    form = CommentForm()
    context = {
        'article' : article,
        'form' : form,
    }
    return render (request, 'mint/detail.html', context)

def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
    return redirect('mint:detail', article_pk)

@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        if article.user == request.user:
            article.delete()
        return redirect('mint:index')
    return redirect('freaks:login')

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('mint:index')
    return redirect('mint:login')