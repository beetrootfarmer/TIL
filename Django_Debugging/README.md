# Django Debugging (문제)

<aside>
❓ 어떻게 수정하면 될까요

</aside>

- 목차

---

## 1. **NoReverseMatch at /accounts/login/**

![스크린샷 2022-10-30 오후 6.18.35.png](Django%20Debugging%20(%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6)%2058d44b7a2ea844869b7e1c3b6add7a34/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-10-30_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_6.18.35.png)

- 수정 전

```python
path('login/', views.login ,name='accounts'),
```

- 수정 후
    - 경로설정에 문제가 있을 때 발생하는 에러
    
    수정할때 잘못 건드렸는지 함수 name이 잘못 설정되어있었다
    
    ```python
    path('login/', views.login ,name='login'),
    ```
    

## 2. NoReverseMatch(2)

![스크린샷 2022-10-30 오후 9.47.57.png](Django%20Debugging%20(%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6)%2058d44b7a2ea844869b7e1c3b6add7a34/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-10-30_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_9.47.57.png)

- 수정 전
    
    ```python
    <form action="{% url 'articles:likes' article_pk %}" method="POST">
    ```
    
- 수정 후
    
    ```python
    <form action="{% url 'articles:likes' article.pk %}" method="POST">
    ```
    

---

## 3. 회원정보 수정이 안됩니다

> 문제 : 수정정보를 입력하고 넘겼는데 index페이지로 넘어감
> 
- view에서 구현한 POST요청 시 form을 저장하는 부분이 작동하지 않음

![스크린샷 2022-10-30 오후 6.39.54.png](Django%20Debugging%20(%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6)%2058d44b7a2ea844869b7e1c3b6add7a34/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-10-30_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_6.39.54.png)

- 수정 전

```html
{% extends 'base.html' %}
{% block content %}
{% load bootstrap5 %}
<h1>회원정보 수정</h1>
<hr>
**<form action="{% url 'articles:index' %}" method="POST">**
  {% csrf_token %}
  {% bootstrap_form form%}
  <button class="btn btn-outline-primary" type="submit" value="수정하기">수정하기</button>
</form>
{% endblock content %}
```

- 수정 후
    - html form에서 작성한 action이 작동되어서 요청이 POST로 받아지지 않음
    - action 제거
    
    ```html
    <form action="" method="POST">
    ```
    

---

## 4. AttributeError

![스크린샷 2022-10-30 오후 9.01.21.png](Django%20Debugging%20(%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6)%2058d44b7a2ea844869b7e1c3b6add7a34/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-10-30_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_9.01.21.png)

- 수정 전
    - 팔로우 버튼을 눌렀을 때 해당 에러가 발생
    
    ```python
    @require_POST
    def follow(request, user_pk):
        if request.user.is_authenticated:
            User = get_user_model()
            person = User.objects.get(pk=user_pk)
            if person != User:
                if person.followers.filter(pk=request.user.pk):
                    person.followers.remove(request.user)
                else:
                    person.followers.add(request.add)
            return redirect('accounts:profile', person.username)
        return redirect('accounts:login')
    ```
    
- 수정 후
    - request로 받은 정보에 사용할 수 없는 속성을 썼을 때
    - Traceback 81에 적힌 부분을 보면 뭐가 잘못됐는지 보임
    
    ```python
    person.followers.add(request.user)
    ```
    

---

## 5. TypeError

![스크린샷 2022-10-30 오후 10.04.46.png](Django%20Debugging%20(%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6)%2058d44b7a2ea844869b7e1c3b6add7a34/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-10-30_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_10.04.46.png)

- 좋아요버튼을 눌렀을 때 에러가 발생
- 수정 전
    
    ```python
    def likes(request, article_pk):
        if request.user.is_authenticated:
            article = Article.objects.get(pk=article_pk)
            if article.like_users.filter(request.user):
                article.like_users.remove(request.user)
            else:
                article.like_users.add(request.user)
            return redirect('articles:index')
        return redirect('accounts:login')
    ```
    
- 수정 후
    - filter()함수에 전달하는 인자 형태가 틀림
    - filter로 나오는건 pk로 조회했기 때문에
        
        `<QuerySet [<User: myezi>]>` 형태로 유저 이름 하나가 들어있어서
        
        exists() 안붙여도 정상적으로 작동함
        
    - 명시적으로 써준듯
    
    ```python
    def likes(request, article_pk):
        if request.user.is_authenticated:
            article = Article.objects.get(pk=article_pk)
            if article.like_users.filter(**pk=request.user.pk**).exists():
                article.like_users.remove(request.user)
            else:
                article.like_users.add(request.user)
            return redirect('articles:index')
        return redirect('accounts:login')
    ```
    

---

## 6. DoesNotExist

![스크린샷 2022-10-30 오후 10.52.49.png](Django%20Debugging%20(%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6)%2058d44b7a2ea844869b7e1c3b6add7a34/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-10-30_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_10.52.49.png)