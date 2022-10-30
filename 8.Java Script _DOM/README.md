# Java Script_DOM

> 학습목표
브라우저에서 문서를 조작하는 메서드를 학습
> 
- 목차

## Browser APIs

웹 브라우저에 내장된 API로 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러가지 유용하고 복잡한 일을 수행

- DOM
- Geolocation API
- WebGL

# DOM

- Document Object Model
- 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
    - 문서구조, 스타일, 내용 등을 쉽게 변경할 수 있게 도움
    - HTML 콘텐츠를 추가, 제거 , 변경하고 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작
- HTML 문서를 구조화하여 각 요소를 객체(object)로 취급
- 단순한 속성접근, 메서드 뿐 아니라 프로그래밍 언어적 특성을 활용한 조작 가능

![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled.png)

- DOM 은 문서를 논리 트리로 표현
- DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일 ,컨텐츠를 변경할 수 있음
- 웹페이지는 일종의 문서
- 웹 브라우저를 통해 내용이 해석되어 화면에 나타나거나 HTML코드 자체로 나타나기도 함
- DOM은 동일한 문서를 표현, 저장, 조작하는 방법을 제공
- DOM은 웹 페이지의 객체 지향 표현이며 JS와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음

### DOM에 접근하기

- 모든 웹 브라우저가 DOM구조를 사용
- DOM이 제공하는 주요 객체를 활용해 문서를 조작하거나 특정 요소를 얻을 수 있음
    - window object
        
        DOM을 표현하는 창
        
        가장 최상위 객체
        
        탭 기능이 있는 브라우저에서 사용
        
        window는 보통 생략 
        
    - document object
        
        브라우저가 불러온 웹 페이지
        
        페이지 컨텐츠의 진입점 역할
        
        윈도우보다 하위객체로 html문서를 의미함
        
        <body>등과 같은 수많은 요소를 포함
        
        

+

파싱(Parsing)

- 구문 분석, 해석
- 브라우저가 문자열을 해석해 DOM Tree로 만드는 과정
    
    ![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%202.png)
    

---

# DOM 조작

### 선택 관련 메서드

- document.querySelector(selector)
    - 제공한 선택자와 일치하는 element 한 개 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null 반환)
- document.querySelectorAll(selector)
    - 제공한 선택자와 일치하는 여러 element를 선택
    - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열로 받음)
    - 제공한 CSS selector를 만족하는 NodeList반환(배열로 사용할 수 있는 객체)

```html
<body>
  <h1 id="title">DOM 조작</h1>
  <p class="text">querySelector</p>
  <p class="text">querySelectorAll</p>
  <ul>
    <li>Javascript</li>
    <li>Python</li>
  </ul>
```

**body > ul > li:nth-child(1)**

![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%203.png)

```
console.log(document.querySelector('#title'))
console.log(document.querySelectorAll('.text'))
console.log(document.querySelector('.text'))
console.log(document.querySelectorAll('body > ul > li'))
```

![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%204.png)

### forEach문 사용가능(NodeList 순회가능)

```jsx
liTags = document.qureySelectorAll('body > ul > li')
liTags.forEach(element =>{
	console.log(element)
})
```

- 실시간으로 반영되지는 않는다 (정적컬렉션)
    - `[document.querySelectorAll()](https://developer.mozilla.org/ko/docs/Web/API/Document/querySelectorAll)`은 정적 `NodeList`를 반환합니다.
    - NodeList의 항목을 순회하거나 리스트의 길이를 캐시해야할 때 구분하는 것이 좋음
    - 정적인 컬렉션을 더 많이 사용한다
- Node.shildNodes는 실시간 (라이브 컬렉션)

## 조작 관련 메서드

### document.createElement(tagName) :(생성)

- 태그를 만드는 메서드

### Node.innerText : (입력)

- 텍스트 컨텐츠로 표현

### Node.appendChild() : (추가)

- 한 Node를 특정 부모Node의 자식 NodeList 중 마지막 자식으로 삽입
- 한번에 오직 하나의 Node만 추가할 수 있음
- 추가된 Node 객체를 반환
- 만약 주어진 Node 가 이미 문서에 존재하는 다른 Node를 참조하면 현재위치에서 새로운 위치로 이동

### Node.removeChild() : 삭제

- DOM에서 자식 노드 제거후 제거된 노드 반환

```html
<body>
  <div style="color: blue;"></div>
  
  <script>
    // 1. 태그생성
    const h1Tag = document.createElement('h1') //createElement가 요소를 반환함
    // 2. 내용작성
    h1Tag.innerText = 'DOMDOMDOMDOMDOMDOM'
    // 3. 태그 선택 후 요소를 자식태그로
    divTag = document.querySelector('div')
    divTag.appendChild(h1Tag)
    // 4. 삭제
    // divTag.remove(h1Tag)
  </script>
</body>
```

### Element.getAttribute(attributeName)

- 해당 요소의 지정된 값을 반환(문자열)
- 인자는 값을 얻고자하는 속성의 이름

### Element.setAttribute(name, value)

- 지정된 요소의 값을 설정
- 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

```jsx
// 1. a태그 생성
const aTag = document.createElement('a')
// 2. 속성추가
aTag.setAttribute('href', 'https://google.com')
// 3. 내용추가
aTag.innerText = '구글'
// 4. 화면에 출력하기위해 div를 선택하고 a태그 담기 
const divTag = document.querySelector('div')
divTag.append(aTag)

// 5. classList를 활용해서 blue클래스가 존재하면 h1Tag에 적용 
const h1Tag = document.querySelector('h1')
h1Tag.classList.toggle('blue') // blue클래스 적용
```

---

# Event

### Event란

프로그래밍하고있는 시스템에서 일어나는 사건 혹은 발생인데 우리가 원한다면 그것들에 어떤 방식으로 응답할 수 있도록 시스템이 말해주는 것 

- 키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등

### Event object

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기위한 객체
- Event발생
    - 사용자 행동 혹은 특성 메서드 호출로 프로그래밍적으로 만들 수도 있음
- DOM요소는 Event를 받고(수신)
- 받은 Event를 (처리) 할 수 있음
    - addEventListener()라는 Event Handler를 사용해 다양한 html요소에 (부착)하게 된다

## Event handler-addEventListener()

```jsx
EventTarget.addEventListener(type, listener)
```

![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%205.png)

- 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정
- Event 를 지원하는 모든 객체(Element, Document, Window)를 대상(Event Target)으로 지정가능
- type
    - 반응 할 Event 유형을 나타내는 대소문자 구분 문자열
    - 대표이벤트 : input, click, submt, scroll
    - 
- listener
    - 지정된 타입의 Event를 수신할 객체
    - JS function 객체(콜백함수)여야함
    - 콜백함수는 발생한 Event의 데이터를 가진 Event기반 객체를 유일한 매개변수로 받음

### 버튼을 누르면 숫자가 증가하도록

```jsx
<body>
  <button id="btn">버튼</button>
  <p id="counter">0</p>
  
  <script>
    const btn = document.querySelector('#btn')
    let countNum = 0
    
    btn.addEventListener('click', function (event){
      console.log(event) // console event 
      const pTag = document.querySelector('#counter')
      countNum += 1
      pTag.innerText = countNum
    })
  </script>
</body>
```

![클릭 이벤트 발생 ](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%206.png)

클릭 이벤트 발생 

![counter변수 증가 확인](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%207.png)

counter변수 증가 확인

### input이벤트 발생시 실시간 출력

```jsx
<body>
  <input type="text" id="text-input">
  <p></p>
  <script>
    const inputTag = document.querySelector('#text-input')
    inputTag.addEventListener('input', function(event) {
      // console.log(event)
      
      const pTag = document.querySelector('p')
      pTag.innerText = event.target.value
      // console.log(event.target)
      // inputTag의 속성값에 접근하는 메서드
    })
  </script>
</body>
```

![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%208.png)

### input에 입력하면 입력값 실시간 출력+ 버튼 클릭시 출력값의 클래스 출력

```jsx
<body>
  <h1>블루블루블루짱</h1>
  <button id="btn">클릭</button>
  <input type="text">

  <script>
   const btn = document.querySelector('#btn')
   btn.addEventListener('click', function(event) {
      const h1Tag = document.querySelector('h1')
      h1Tag.classList.toggle('blue')
   })
   const inputTag = document.querySelector('input')
    inputTag.addEventListener('input', function(event) {
      const h1Tag = document.querySelector('h1')
      h1Tag.innerText = event.target.value
    })
  </script>
</body>
```

![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%209.png)

![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%2010.png)


### Event 취소

### event.preventDafault

```jsx
<body>
  <div>
    <h1>정말 중요한 내용</h1>
  </div>

  <script>
   const h1Tag = document.querySelector('h1')
   h1Tag.addEventListener('copy', function(event){
    event.preventDefault()
    alert('복사 할 수 없습니다!!')
   })
  </script>
</body>
```

![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%2012.png)

---

## Event 종합 실습_로또번호 출력

```jsx
<body>
  <h1>로또 추천 번호</h1>
  <button id="lotto-btn">행운 번호 받기</button>
  <div id="result"></div>

  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  
  <script>
    const btn = document.querySelector("#lotto-btn")
    btn.addEventListener('click', function(event){
      
      // 공 컨테이너 생성
      const ball = document.createElement('div')
      ball.classList.add('ball-container')
      
      // 랜덤한 숫자 6자리 생성 
      // lodash 라이브러리 사용 
      const numbers = _.sampleSize(_.range(1, 46), 6)
      console.log(numbers)
    })
  </script>
</body>
```

![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%2013.png)

```html
<!DOCTYPE html>
<html lang ="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>lotto</title>
  <style>
    /* 스타일은 수정하지 않습니다. */
    .ball {
      width: 10rem;
      height: 10rem;
      margin: .5rem;
      border-radius: 50%;
      text-align: center;
      line-height: 10rem;
      font-size: xx-large;
      font-weight: bold;
      color: white;
    }
    .ball-container {
      display: flex;
    }
  </style>
</head>
<body>
  <h1>로또 추천 번호</h1>
  <button id="lotto-btn">행운 번호 받기</button>
  <div id="result"></div>

  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  
  <script>
    const btn = document.querySelector("#lotto-btn")
    btn.addEventListener('click', function(){
      
      // 공 컨테이너 생성
      const ballContainer = document.createElement('div')
      ballContainer.classList.add('ball-container')
        
      // 랜덤한 숫자 6자리 생성 
      // lodash 라이브러리 사용 
      const numbers = _.sampleSize(_.range(1, 46), 6)
      // console.log(numbers)

      // 공 만들기
      numbers.forEach((number) => {
        const ball = document.createElement('div')
        ball.innerText = number
        ball.classList.add('ball')
        ball.style.backgroundColor = 'crimson'
        ballContainer.appendChild(ball)
      })
      // 공 컨테이너는 결과 영역의 자식으로 
      const resultDiv = document.querySelector('#result')
      resultDiv.appendChild(ballContainer)
    })

  </script>
</body>
</html>
```


![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%2015.png)

---

### 입력값 리스트로 만들기

```jsx
<body>
  <form action="#">
    <input type="text" class="inputData">
    <input type="submit" value="Add">
  </form>
  <ul></ul>

  <script>
    const formTag = document.querySelector('form')
    const addTodo = function(event){
      // console.log(event)
      event.preventDefault()
      const inputTag = document.querySelector('.inputData')
      const data = inputTag.value
      console.log(data)

      // 내용이 있을 때 추가 되도록
      if (data.trim()) {
        const liTag = document.createElement('li')
        liTag.innerText = data
  
        const ulTag = document.querySelector('ul')
        ulTag.appendChild(liTag)
        event.target.reset()
      } else {
        alert('내용을 입력하세요!')
      }
    }

    // 콜백함수로 만들어서 사용하기 
    formTag.addEventListener('submit', addTodo)
  </script>
</body>
```

![event.target.reset() 적용전](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%2016.png)

event.target.reset() 적용전

![event.target.reset() 적용후](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%2017.png)

event.target.reset() 적용후

---

# this

- 어떠한 object를 가리키는 키워드
    - java의 this와 python 의 self는 인스턴스 자기자신을 가리킴
- 함수가 호출 될 때 this를 암묵적으로 전달받음
- JS는 함수의 호출 방식에 따라 this에 바인딩되는 객체가 달라짐
- 함수가 어떻게 호출되는지에 따라서 동적으로 결정된다

### this INDEX

### 전역 문맥에서 this

- 브라우저의 전역객체인 window를 가리킴
- 모든 객체의 유일한 최상위 객체를 의미

### 함수 문맥에서 this

### 단순 호출

- 전역 객체를 가리킴
- 브라우저에서는 window, Node.js에서는 global을 의미

### Method(객체의 메서드로서)

- 메서드를 선언하고 호출하면 객체의 메서드이므로 해당 객체가 바인딩된다

```jsx
const myObj = {
	data : 1,
	myFunc() {
		console.log(this) //myObj
		console.log(this.data) //1
	}
}
myObj.myFunc() //myObj
```

### Nested

- forEach의 콜백함수에서 this는 메서드의 객체를 가리키지 못하고 전역객체 window를 가리킴
- 단순 호출방식으로 사용되었기 때문
- 이를 해결하기위해 등장한 함수 표현식이 “화살표함수”

![Untitled](Java%20Script_DOM%209a2aea8c7c244d1a8f81d7dfed2934c2/Untitled%2018.png)

- 화살표함수에서 this는 자신을 감싼 정적 범위
- 자동으로 한 단계 상위의 scope의 context를 바인딩

```jsx
const myObj = {
	numbers: [1],
	myFunc() {
		console.log(this) //myObj
		this.numbers.forEach((number) => {
			console.log(number) //1
			console.log(this) //myObj
		})
	}
}
myObj.myFunc()
```

- 화살표 함수는 호출의 위치와 상관없이 상위스코프를 가리킴
- Lexical scope
    - 어디에 선언하였는지에 따라 결정
    - Static scope라고도 하며 대부분의 프로그래밍 언어에서 따르는 방식
- 함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장

**BUT**

- addEventListener의 한 단계 상위 스코프는 전역이기 때문에 (window)
- addEventListener의 콜백함수는 function키워드를 사용하기