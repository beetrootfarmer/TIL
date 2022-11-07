from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def index(request):
    # request에는 모든 요청정보가 들어있다.
    # path 함수에 views.index 함수 정보 넘겨주면서
    # path 함수 내부에서 호출할 때 첫번째 인자 넘겨준다.

    # SELECT * FROM articles_article
    # <Query SET [<Article object(1)>, ]>
    articles = Article.objects.all()            
    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context) # templates/articles/index.html
@login_required
def create(request):
    if request.method ==  'POST':
        # 사용자가 POST 요청을 보낼 때 같이 보낸 정보들
        # model에 대한 정보와 form에대한 정보 모두 가지고있는
        # ArticleForm에게 사용자의 요청 정보를 같이 넘겨줘서
        form = ArticleForm(request.POST)    # key, value 값 알아서 매칭해줌
        # 사용자가 보낸 정보다 정상적인 데이터인지 확인
        # 왜 ? sqlite 스키마 무시하고 데이터 넣는대로 다 받아버림;
        # DB에 넣기 전에 사용자가 입력한 데이터를 확인..!
        if form.is_valid(): 
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk): # (주의) url에 정의한 변수명과 일치해야함
    article = Article.objects.get(pk= article_pk)
    # article에 pk 값에 일치하는 article.title, article.content 가 들어있음
    # comments = article.comment_set.all()
    form = CommentForm()
    context = {
        'article' : article,
        'form' : form,
        # 'comment' : comments,
    }
    return render(request, 'articles/detail.html', context)
    
def comment_create(request, article_pk):
    article =  Article.objects.get(pk=article_pk)
    if request.method ==  'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # comment 객체 생성
            # 저장해서 생성하는데 db에 반영이 안되도록
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
    return redirect('articles:detail',article_pk)

@require_POST
# @login_required
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        if article.user == request.user:  # 게시글이 가진 유저정보와 요청을 보낸 유저정보가 일치하는지 확인
            article.delete()
        return redirect('articles:index')
    return redirect('accounts:login')