# Java Script_ 비동기처리 axios

- 목차

# 동기와 비동기

## 동기 Synchronous

- 모든 일을 순서대로 하나씩 처리하는 것
- 순서대로 처리한다 == 이전 작업이 끝나면 다음 작업을 시작한다
- python 코드가 위에서부터 순서대로 진행되는 것이 동기식(정확히는 blocking의 개념)
- 요청과 응답을 동기식으로 처리? 요청을 보내고 응답이 올때까지 기다렸다가 다음 로직을 처리
- non-block이면서 동기적으로 작용한다 : 함수가 끝나기 전에 다른 함수를 실행하는데 제어권을 넘겨주지는 않으면서 이전 함수의 진행상황을 계속 확인하는 것
- block이면서 동기적으로 작용한다  : 기존 함수의 리턴값을 필요로해서 제어권을 넘겨주고 새로운 함수가 실행이 완료될 때까지 기다린다

## 비동기 Asynchronous

- 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것(병렬적 수행)
- 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
    - 메일 전송을 누르면 목록 화면으로 전환되지만 메일을 보내는 작업은 병렬적으로 뒤에서 처리된다
- block이면서 비동기 :  커피주문하고 대기한다. 기존 함수의 리턴값을 필요로하지는 않지만 제어권을 넘기고 실행을 멈춘다
- non-block 비동기 : 커피 주문하고 다른 일 하다가 커피가 만들어지면 받는다. 제어권을 넘겨주지 않으면서 자신의 함수를 계속 실행한다

![Untitled](Java%20Script_%20%E1%84%87%E1%85%B5%E1%84%83%E1%85%A9%E1%86%BC%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5%20axios%20a32616b47fce4a798667b76cdc661b72/Untitled.png)

## 비동기를 사용하는 이유

### 사용자 경험

- 동기식 처리는 특정 로직이 실행되는 동안 다른 로직을 차단하기때문에 프로그램이 응답하지 않는 듯한 UX를 만들게된다
- 비동기식으로 처리하면 먼저 처리되는 부분부터 보여줄 수 있으므로 사용자 경험에 긍정적인 효과를 ㅂ로 수 있음

### Single Thread 언어

- JavaScript는 한번에 하나의 일만 수행할 수 있는 Single Thread 언어로 동시에 여러 작업을 처리할 수 없음
- JS는 하나의 작업을 요청한 순서대로 처리할 수 밖에 없다

---

# JavaScript의 비동기 처리

### JavaScript Runtime

- JavaScript 자체적으로는 비동기 처리를 할 수 없는데
- 특정 언어가 동작할 수 있는 환경을 런타임이라고한다
- JS에서 비동기와 관련한 작업은 브라우저 또는 Node환경에서 처리
- 브라우저 환경에서 비동기 동작의 구성요소
    - JavaScript Engine의 Call Stack
    - Web API
    - Task Queue
    - Event Loop

### 브라우저에서 비동기 처리 동작 방식

1. 모든 작업은 Call Stack(LIFO)으로 들어간 후 처리된다
2. 오래걸리는 작업이 Call Stack으로 들어오면 Web API로 보내 별도로 처리하도록 한다
3. Web API에서 처리가 끝난 작업들은 곧바로 Call Stack 으로 들어가지 못하고 Task Queue(FIFO)에 순서대로 들어간다                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
4. Event Loop가 Call Stack이 비어있는 것을 계속 체크하고 Call STack이 빈다면 Task Queue에서 가장 오랜된 작업을 Call Stack으로 보낸다 

![다른 task는 Call Stack에서 먼저 처리된다](Java%20Script_%20%E1%84%87%E1%85%B5%E1%84%83%E1%85%A9%E1%86%BC%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5%20axios%20a32616b47fce4a798667b76cdc661b72/Untitled%201.png)

다른 task는 Call Stack에서 먼저 처리된다

![WebAPI에서 처리가 끝나면 Task Queue로 들어간다](Java%20Script_%20%E1%84%87%E1%85%B5%E1%84%83%E1%85%A9%E1%86%BC%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5%20axios%20a32616b47fce4a798667b76cdc661b72/Untitled%202.png)

WebAPI에서 처리가 끝나면 Task Queue로 들어간다

![Event Loop가 감시를 하다가 Task Queue에 먼저 온 순서대로 보내는데 조건은 Call Stack이 비워지는 것. Call Stack 이 비워질 때까지 기다려야하기때문에 3초 뒤에 실행을 보장하지 못한다.](Java%20Script_%20%E1%84%87%E1%85%B5%E1%84%83%E1%85%A9%E1%86%BC%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5%20axios%20a32616b47fce4a798667b76cdc661b72/Untitled%203.png)

Event Loop가 감시를 하다가 Task Queue에 먼저 온 순서대로 보내는데 조건은 Call Stack이 비워지는 것. Call Stack 이 비워질 때까지 기다려야하기때문에 3초 뒤에 실행을 보장하지 못한다.

- setTimeout(function() { console.log(’gogo’) }, 0 )
    
    지연시간을 0으로 설정하는 것은 Web API에서 딜레이 시간이기 때문에 최소 지연시간이 된다. 결국 Call Stack이 비워질 때까지 기다려야하는것은 같다
    

---

# Axios 라이브러리

## Axios

- JS의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능하나 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node환경을 npm을 이용해서 설치 후 사용할 수 있고
browser환경은 CDN을 이용해서 사용할 수 있음

## Axios 사용하기

```jsx
axios.get("요청할 URL")
	.then(성공하면 수행할 콜백함수)
	.catch(실패하면 수행할 콜백함수)
```

### 파이썬의 동기식 처리 , JS의 비동기식 처리

- 파이썬

![Untitled](Java%20Script_%20%E1%84%87%E1%85%B5%E1%84%83%E1%85%A9%E1%86%BC%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5%20axios%20a32616b47fce4a798667b76cdc661b72/Untitled%204.png)

![Untitled](Java%20Script_%20%E1%84%87%E1%85%B5%E1%84%83%E1%85%A9%E1%86%BC%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5%20axios%20a32616b47fce4a798667b76cdc661b72/Untitled%205.png)

- 고양이 API code
    
    ```jsx
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <button>야옹아 이리온</button>
    
      <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
      <script>
        console.log('고양이는 야옹')
        const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
        const btn = document.querySelector('button')
    
        btn.addEventListener('click', function () {
          axios.get(catImageSearchURL)
            .then((response) => {
              imgElem = document.createElement('img')
              imgElem.setAttribute('src', response.data[0].url)
              document.body.appendChild(imgElem)
            })
            .catch((error) => { 
              console.log('실패했다옹')
            })
            console.log('야옹야옹') 
        })
      </script>
    </body>
    </html>
    ```
    

- axios는 비동기로 데이터 동신을 가능하게 하는 라이브러리
- 같은 방식으로 우리가 배운 Django REST API로 요청을 보내서 데이터를 받아온 후 처리할 수 있음

## 강아지사진 생성기

```jsx
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dog API</title>
  <style>
    img {
      height: 500px;
    }
  </style>
</head>

<body>
  <h1>Dog API</h1>
  <img src="" alt="dog">
  <br>
  <button>Get dog</button>

  <!-- axios CDN을 삽입한다. -->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

  <script>
    const API_URI = 'https://dog.ceo/api/breeds/image/random'

    function getDog() {
      // axios를 사용하여 API_URI로 GET 요청을 보낸다.
      axios.get(API_URI)
      // .then 메서드를 통해 요청이 성공적인 경우의 콜백함수를 정의한다.
      .then((response) => {
          imgElem = document.querySelector('img')
          // 응답객체의 데이터에서 이미지에 대한 리소스를 img 요소의 src 속성으로 할당한다.    
          imgElem.setAttribute('src', response.data.message)
          document.body.appendChild(imgElem)
        })
        .catch((error) => { 
          console.log('실패했개')
        })
        console.log('멍멍') 
    }

    const button = document.querySelector('button')
    button.addEventListener('click', getDog)

  </script>
</body>

</html>
```

---

# Callback과 Promise

### 비동기처리의 단점

- 작업이 완료되는 순서에 따라 처리하기때문에 개발자 입장에서 실행순서가 불명확함
- 그렇기 때문에 실행결과를 예상하면서 코드를 작성할 수 없게 함

⇒ 콜백함수를 사용함으로써 보완

## 콜백함수

- 다른함수의 인자로 전달되는 함수
- 동기, 비동기 상관없이 사용가능
- 비동기 작업이 완료된 후 실행할 작업을 명시하는 데 실행할 작업을 명시하는 데 사용되는 콜백함수를 비동기콜백(asynchronous callback)이라 부름

```jsx
const btn = document.querySelector('button')
btn.addEventListener('click',() => {
	alert('Completed')
})
```

```jsx
from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.index),
]
```

### 콜백함수를 사용하는 이유

- 특정한 조건 혹은 행동에 대해 호출되도록 작성할 수 있음
- “요청시” “이벤트 발생시” “데이터 받을 시” 등의 조건
- 비동기 처리를 순차적으로 동작할 수 있게 한다

### 콜백지옥

- 연쇄적인 비동기 작업을 순서대로 동작할 때
- 비동기 처리를 순차적으로 실행하기 위해 반드시 필요한 콜백을 작성할 때 마주하는 문제
- 피라미드처럼 생겨서 파멸의 피라미드라고도 부른다(Pyramid of doom)
- 코드의 가독성을 해치고 유지보수가 어려워짐

## 프로미스 (Promise)

- 콜백지옥 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
- “작업이 끝나면 실행시켜줄게”라는 약속
- 비동기 작업의 완료 또는 실패를 나타내는 객체
- Promise 기반의 클라이언트가 바로 Axios 라이브러리
    - “Promise based HPPT client for the browser and node.js”
    - 
    - 실패에 대한 약속 catch()

### then(callback)

- 요청한 작업이 성공하면 callback 실행
- callback은 이전 작업의 성공 결과를 인자로 전달받음

### catch(callback)

- then()이 하나라도 실패하면 callback 실행
- callback 은 이전 작업의 실패 객체를 인자로 전달받음

- then과 catch 모두 항상 promise 객체를 반환하기때문에 chaining을 할 수 있음
- axios로 처리한 비동기 로직이 항상 promise객체를 반환하기때문에 then을 계속 이어나가면서 작성할 수 있는 것

### 비동기방식과 Promise

- 프로미스 방식은 비동기처리를 마치 우리가 일반적으로 위에서 아래로 적는 방식으로 코드를 작성할 수 있음

### Promise가 보장하는 것

(비동기 콜백과 비교해서)

1. Call back함수는 JavaScript의 EventLoop가 현재 실행중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
    - Promise Call back함수는 Event Queue에 배치되는 엄격한 순서로 호출된다
2. 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
3. .then()을 여러번 사용하여 여러개의 callback 함수를 추가할 수 있음 (Chaning)
    - 각각의 callback은 주어진 순서대로 하나하나 실행하게 된다
    - Chaning은 Promise의 가장 뛰어난 장점

### Axios 권장 표기 방식

```jsx
btn.addEventListener('click', function(){
	axios({
		method : 'post',
		url : catImageSearchURL,
	})
		.then((response) => {
			imgElem = document.createElement('img')
			return imgElem
		})
		.then((imgElem) => {
			imgElem.setAttribute('src', response.data[0].url_
			document.log('실패했다옹')
		})
		console.log('야옹야옹')
```

일반 표기방식

```jsx
 btn.addEventListener('click', function(){
	axios.get(catImageSearchURL)
		.then((response) => {
			imgElem = document.createElement('img')
			return imgElem
		})
		.then((imgElem) => {
			imgElem.setAttribute('src', response.data[0].url_
			document.log('실패했다옹')
		})
		console.log('야옹야옹')
```

---

# AJAX

- 페이지 전체를 새로고침 하지 않고서도 수행되는 비동기성
- 서버의 응담에 따라 전체 페이지가 아닌 일부분만을 업데이트 할 수 있음
1. 페이지 새로고침 없이 서버에 요청
2. 서버로부터 응답을 받아 작업을 수행

## AJAX로 팔로우기능

1. axios cdn 추가
    
    ```jsx
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    ```
    
2. form tag 수정
    - action과 method 지워주고 axios로 처리할것임
    - *axios로 POST 요청을 보낼 것임*
    
    ```jsx
    <form id="follow-form">
    ```
    
3. script로 form태그에 EvenetListener 달아주기
    - *AJAX 요청을 보내기 위해 axios 사용*
    - *POST 요청을 /accounts/follow url로 보낼 것임*
    - *상대경로 앞쪽 localhost:8000은 생략하고 / 로 시작하는 경로*
    - url로 user_pk를 담아줘야하는데 js에서 사용자 정보를 가져올 수 없어서 form 태그 수정
        
        ```jsx
        <form id="follow-form" data-user-id="{{person.pk}}">
        ```
        
        - js에서 가지고오기
        
        ```jsx
        const userId = event.target.dataset.userId # 카멜케이스 주의
        =>
        const { userId } = event.target.dataset # 구조분해할당. 새로 만드는 변수명과 같으면 이렇게 사용가능
        
        axios({
            method:'post',
            url: `/accounts/${userId}/follow`,
          })
        ```
        
    - csrf token 추가
        
        ```jsx
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
        
        headers : {'X-CSRFToken' : csrfToken}, //axios header에 토큰 담아주기
        ```
        
    - view에서 json 데이터를 응답받아서 js에서 처리하기
        
        ```python
        # views.py
        if person.followers.filter(pk=me.pk).exists(): # 저 사람의 followers목록에 내가 있으면 언팔
            person.followers.remove(me)
            is_followed = False
        else: # 저 사람의 followers목록에 내가 있으면 팔로우
            person.followers.add(me)
            is_followed = True
        # JSON데이터 응답
        # follow boolean 을 구분해서 dict형태로 보내줄 것
        context = {
            'is_followed' : is_followed
        }
        ```
        
    - 버튼에 팔로우, 언팔로우 글자 바꿔주기위해 then(function 구현
        - *성공하면 -> 팔로우/언팔로우 글자 바꾸고, 팔로워 수 바꾸기*
            - 팔로우 버튼 선택해서 innerText 혹은 value 변경
            - 팔로워 수 바꾸기
        
        ```jsx
        .then(function (response){
              console.log(response)
              // 원래 로직대로라면 response에 html이 담겨있는데
              // 팔로우 여부 boolean으로 필요함. view처리
              const isFollowed = response.data.is_followed
              const followersCount = response.data.followers_count
              const followBtn = document.querySelector('#follow-form > input[type=submit]')
              const followersCountSpan = document.querySelector('#followers-count')
              followBtn.value = isFollowed ? '언팔로우' :'팔로우'
                // 팔로워 수 바꾸기
              followersCountSpan.innerText = followersCount
            })
        ```
        
        ```html
        	팔로워 수 : <span id="followers-count">{{ followers|length }}</span>
        ```
        

---

## 좋아요 기능 AJAX로 구현

1. axois cdn 추가
    
    ```jsx
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    ```
    
2. form tag 수정
    
    ```html
    <form class="like-form" data-article-id="{{ article.pk }}">
    ```
    
3. form tag select하고 submit event 막기
    - forEach로 여러개의 form을 선택할 것이기 때문에 **querySelectorAll()**을 사용해야한다
    
    ```jsx
    const form = document.querySelectorAll('form')
        form.addEventListener('submit', function(event){
          event.preventDefault()
        })
    ```
    
4. article Id formtag에서 지정하고 js에서 가져오기
    
    ```jsx
    <form class="like-form" data-article-id="{{ article.pk }}">
    ```
    
    ```jsx
    const { articleId } = event.target.dataset
    ```
    
5. csrf token 가져오기
    
    ```jsx
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
    ```
    
6. axios로 데이터 전달하기
    
    ```jsx
    axios({
        method:'post',
        url: `/accounts/${userId}/follow`,
    		headers : {'X-CSRFToken' : csrfToken}, //axios header에 토큰 담아주기
      })
    ```
    
7. view에서 json 형태로 좋아요 여부 전달하기
    - get_object_or_404를 사용하는 경우와 Article.objects.get을 사용하는 경우 차이??
    
    ```jsx
    @require_POST
    def likes(request, article_pk):
        if request.user.is_authenticated:
            article = Article.objects.get(pk=article_pk)
            # person이 좋아요를 눌렀으면 좋아요 취소
            if article.like_users.filter(pk=request.user.pk).exists():
                article.like_users.remove(request.user)
                is_liked = False
            # 좋아요를 누르지 않았으면 좋아요 
            else:
                article.like_users.add(request.user)
                is_liked = True
            context = {
                'is_liked' : is_liked
            }
            return JsonResponse(context)
        return redirect('accounts:login')
    ```
    
8. 받은 데이터로 좋아요 버튼 글자바꾸기 + 좋아요 수 변하기 
    
    ```jsx
    <script>
        // CODE HERE
        const forms = document.querySelectorAll('form')
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value // id 나 class는 접근법이 정해져있고 모든 속성에 대해 접근할 때는 []형태로 접근할 수 있다 . 여기에는 token난수값이 담긴다
        
        forms.forEach((form) => {
          form.addEventListener('submit', function(event){
            event.preventDefault()
            const {articleId} = event.target.dataset
    
            axios({
              method:'post',
              url:`/articles/${articleId}/likes/`, // 누가 좋아요했는지 표시
              headers : {'X-CSRFToken' : csrfToken},
            })
            .then(function(response){
              console.log(response)
              const isLike = response.data.is_liked
              const likeBtn = document.querySelector(`#like-${articleId}`) // id는 당연히 문자열과 숫자열을 같이 써서 숫자만으로 사용하지 않도록 했음 . 그래서 이렇게 표현!
              const likeCount = response.data.is_liked_count
              console.log(response)
              likeBtn.innerText = isLike ? '좋아요 취소' : '좋아요'
              const likeCountSpan = document.querySelector(`#like-count-${articleId}`)
              likeCountSpan.innerText = likeCount
            })
          })
        })
      </script>
    ```
    
9. *# 상태코드를 axios에 401 전달하고, catch error후 로그인 페이지로 전달하기*
    - HTTPResponse로 상태코드 리턴
    - location.href 로 페이지 다이렉트
    
    ```python
    # views.py
    from django.http import JsonResponse, HttpResponse
    
    return HTTPResponse(status = 401)
    ```
    
    ```jsx
    .catch(function(error) {
      console.log(error)
      if (error.response){
        alert('로그인하세요')
        location.href="/accounts/login/"
       }
    })
    ```
    
    - error 분기 처리
    
    ```jsx
    .catch(function(error) {
    	if (error.response.status === 401 ) {
    		alert('로그인하세요')
    		window.location.href="/accounts/login/"
    	} elif (error.response.status === 403)
    	  alert('권한이 없습니다')
       }
    })
    ```
    

---

### 파비콘 적용

```jsx
<link rel="shortcut icon" href="http://사용자도메인명/favicon.ico" type="image/x-icon" />
```

---