# REST API (1)

# API

> Application Programming Interface
> 
- 애플리케이션과 프로그래밍으로 소통하는 방법
    - 개발자가 프로그래밍 언어로 기능을 만들어 제공하는
- API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 사이의 간단한 계약(인터페이스)
- API는 복잡한 코드를 추상화해서 대신 사용할 수 있는 구문을 제공
    - 예를들어.. 집에 전기를 공급할 때 플러그를 소켓에 꽂으면 작동
    - 우리가 직접 배선을 하지 않음

### Web API

- 현재 웹개발은 여러 OPEN API를 활용하는 추세
- API는 다양한 타입의 데이터를 응답 HTML, XML, JSON
    - 주로 사용하는 것은 JSON

### REST

- Representational State Transfer
- REST 원리를 따르는 시스템을 RESTful 하다고 부름
- REST의 기본 아이디어는 리소스 즉 자원
    - 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술

### REST에서 자원을 정의하고 주소를 지정하는 방법

1. 자원의 식별 URI
2. 자원의 행위 HTTP Method
3. 자원의 표현 
    - 자원과 행위를 통해 궁극적으로 표현되는 결과물
    - JSON으로 표현된 데이터를 제공

### JSON

- JSON is light-weight interchange…
- JavaScript 표기법을 따른 단순문자열
- 파이썬 딕셔너리, JS objecet처럼 C계열 언어가 가지고 있는 자료구조로 쉽게 변환할수있는 key-value형태의 자료구조
- 사람이 읽고쓰기 쉽고 기계가 파싱(해석&분석)하고 만들어내기 쉽기 때문에 현재 API에서 가장 많이 사용하는 데이터타입

## 다양한 방법으로 JSON 응답하기

1. HTML 응답
2. JsonResponse()를 사용한 JSON 응답
    - 문서를 응답하는것이 아니라 JSON데이터를 응답해보기
    - 장고가 기본적으로 제공하는 JsonResponse 객체를 활용하여 파이썬 데이터타입을 손쉽게 JSON으로 변환하여 응답가능
    
    ```python
    from django.http.response import JsonResponse
    
    def article_json_1(request):
        articles = Article.objects.all()
        articles_json = []
    
        for article in articles:
            articles_json.append(
                {
                    'id': article.pk,
                    'title': article.title,
                    'content': article.content,
                    'created_at': article.created_at,
                    'updated_at': article.updated_at,
    
                }
            )
        return JsonResponse(articles_json, safe=False) # dictionary가 아니면 safe옵션을 붙여줘야한다
    ```
    
3. Django Serializer를 사용한 JSON응답
    - 장고의 내장 HttpResponse()를 활용한 JSON응답
    - 이전에는 JSON의 모든 필드를 하나부터 열까지 작성해야하지만 이제는 그렇지 않음!
    
    ```python
    from django.http.response import JsonResponse, HttpResponse
    from django.core import serializers
    
    def article_json_2(request):
        articles = Article.objects.all()
        data = serializers.serialize('json', articles)
        return HttpResponse(data, content_type='application/json')
    ```
    
4. Django REST framework 를 사용한 JSON응답
    - DRF사용
    
    ```python
    from rest_framework import serializers
    from .models import Article
    
    class ArticleSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Article
            fields = '__all__'
    ```
    
    ```python
    @api_view()
    def article_json_3(request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    ```
    
    ### response 방식
    
    ```python
    python pip install requests
    ```
    
    ```python
    # gogo.py
    
    import requests
    from pprint import pprint
    
    response = requests.get('http://127.0.0.1:8000/api/v1/json-3/')
    result = response.json()
    
    pprint(result)
    # pprint(result[0])
    pprint(result[0].get('title'))
    ```
    
    요청데이터를 response에 담아서 json 으로 변환하는 과정 
    
    서버 켜고 > terminal split view > python gogo.py(파일실행)
    
    ⇒ result에 json이 담겨있는 것을 확인 할 수 있음
    

## Serialization

- 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고
- 어떠한 언어나 환경에서도 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 변환 포맷은 보편적으로 json을 사용
- Django의 serialize()는 Queryset및 Model Instance와 같은 데이터를 json으로 변환할 수 있는 python 데이터 타입으로 만들어줌
    - 데이터를 parsing해주는 역할

## Django REST framework(DRF)

- 장고에서 Restful API서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- Wdb API구축을 위한 강력한 toolkit을 제공
- REST framework를 작성하기 위한 여러 기능을제공
- DRF의 serializer는 Django의 Form및 ModelForm 클래스와 매우 유사하게 작동

## RESTframework 환경설정

- requirements.txt / settings.py
    
    ```python
    # requirements.txt
    asgiref==3.5.2
    Django==3.2.13
    django-extensions==3.2.1
    djangorestframework==3.14.0
    pytz==2022.4
    sqlparse==0.4.3
    ```
    
    ```python
    # settings.py
    """
    Django settings for my_api project.
    
    Generated by 'django-admin startproject' using Django 3.2.12.
    
    For more information on this file, see
    https://docs.djangoproject.com/en/3.2/topics/settings/
    
    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/3.2/ref/settings/
    """
    
    from pathlib import Path
    
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
    
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-@$8x-(6upil1k&!fs3p^+_uk@)$yi)-hz-nu=634c9x6=69l06'
    
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    
    ALLOWED_HOSTS = []
    
    # Application definition
    
    INSTALLED_APPS = [
        'articles',
        'django_extensions',
        'rest_framework',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    
    ROOT_URLCONF = 'my_api.urls'
    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    
    WSGI_APPLICATION = 'my_api.wsgi.application'
    
    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    
    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
    
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]
    
    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/
    
    LANGUAGE_CODE = 'en-us'
    
    TIME_ZONE = 'UTC'
    
    USE_I18N = True
    
    USE_L10N = True
    
    USE_TZ = True
    
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/
    
    STATIC_URL = '/static/'
    
    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
    
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    ```
    
- models.py
    
    ```python
    from django.db import models
    
    # Create your models here.
    class Article(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
    class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```
    
- DRF설치
    
    ```python
    $ pip install djangorestframework
    ```
    
- url
    
    ```python
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('articles/', views.article_list),
        path('articles/<int:article_pk>/', views.article_detail),
        path('comments/', views.comment_list),
        path('comments/<int:comment_pk>/', views.comment_detail),
        path('articles/<int:article_pk>/comments/', views.comment_create),
    ]
    ```
    

## serializers.py

```python
from rest_framework import serializers # drf가 제공하는 model serializer
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```

- ModelSerializer클래스는 모델 필드에 해당 필드가 있는 Serializer클래스를 자동으로 만들 수 있는 shortcut을 제공
    1. Model 정보에 맞춰 자동으로 필드 생성
    2. serializer에 대한 유효성 검사기를 자동으로 생성
    3. .create() 및 .update()의 간단한 기본구현이 포함된다

---

## ‘api_view’ decorator

- DRF view 함수가 응답해야하는 HTTP 메서드 목록을 받음
- 기본적으로  GET메소드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답

### GET

- 조회
- DRF에서 api_view데코레이터 작성은 필수

### POST

- 게시글 생성
- 데이터 생성 성공시 201

### DELETE

- 게시글 삭제
- 데이터 삭제 성공시 204 No Content

### PUT

- 수정
- 수정 성공시 200OK

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST']) # @api_view() 이렇게 작성하면 GET이 기본값
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True) # 단일데이터가 아닐때 many=True필수 
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 위의 400 status 설정 코드 대신에 raise_exception=True 로 예외catch~
```

```python
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
				# get() 함수를 썼을 때 pk값이 존재하지 않으면 여기서 코드 에러 발생..
				# get_object_or_404() 는 pk값이 존재하지 않을 때 404에러를 전달하는 shortcurs
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

---

## CommentSerializer

```python
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) # 유효성 검사에서는 제외하고 읽기전용으로  
```

```python
@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

---

## 역참조 데이터 조회

1. 특정 게시글에 작성된 댓글 목록 출력 _ override

2. 특정 게시글에 작성된 댓글 개수 출력 _ 새로운 필드 추가

```python
class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
			# => 역참조 대상의 pk값만 가져오는 함수 
    comment_set = CommentSerializer(many=True, read_only=True)
			# => comments 필드 전체를 가져오는 방법!
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
			# => 새로운 필드를 만드는 것!! source='ORM명령어'

    class Meta:
        model = Article
        fields = '__all__'
				# read_only_fields = ('comment_set','comment_count',)
				# override 되거나 새로만든 필드는 Meta클래스 내에서 read_only 처리할 수 없음 
```

---

## Article-Comment 구조 RESTful하게 만들기

```python
# model
class Article(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    #like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
```

```python
# urls
path('article/',views.article_list),
path('article/<int:article_pk>/', views.article_detail),
path('article/<int:article_pk>/comment/', views.create_comment)
```

```python
# serialize
from rest_framework import serializers
from .models import Article,Comment
 
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Article
        fields = '__all__'
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title', 'content')
```

```python
# views

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleListSerializer(article,many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method =='DELETE':
        article.delete()
        return Response('삭제되었습니다',status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```