from importlib.metadata import requires
from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def index(request):
    articles  = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm
    context = {
        'form':form,
    }
    return render(request, 'articles/new.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        if article.user == request.user:
            article.delete()
        return redirect('articles:index')
    return redirect('accounts:login')

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk) 
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)
