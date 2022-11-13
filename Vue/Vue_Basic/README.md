# Vue Basic

## 목차
- [Vue Intro](#-vue-intro)
  - [FrontEnd(FE) Framework](#-FrontEnd(FE)-Framework)
  - [Web App](#Web-App)
  - [SPA](#SPA)
  - [CSR(Client Side Rendering)](#CSR(Client-Side-Rendering))
    - [CSR 방식을 사용하는 이유?](#csr-방식을-사용하는-이유?)
    - [CSR은 만능일까?](#CSR은-만능일까?)
    - [SEO](#SEO)
    -### Vue CDN
    - ### v-model : input에 입력하는 값 화면에 보여주기
    - ### Vue2 vs Vue3
# Vue instance
## MVVM Pattern
### view와 model 이 직접적으로 연결되어있지 않음!
## 생성자 함수
### el (element)
### data
### method
### 메서드를 정의할 때 Arrow Function 사용X

# Basic of Syntax

## Text interpolation
## Directives
### v-text
### v-html
### v-show
### v-if
### v-show VS v-if
### v-for
### v-for 사용시 반드시 key속성값을 각 요소에 작성
### v-on
### v-bind
### V-model

## Vue advanced

### computed
## watch
## filter

## Vue Style Guide
### v-if 와 v-for를 같이 사용하지 않기

### lodash cdn
### Lodash 사용해서 랜덤한 값 표출하기
---
# Vue Intro

## FrontEnd(FE) Framework

Vue.js === JavaScript Font-end Framework

## Web App

SPA(Single Page Application)을 만들 때 사용하는 도구

웹 브라우저에서 실행되는 어플리케이션 소프트웨어

웹페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 App처럼 보이는 것

## SPA

서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식

**어떻게 한 페이지로 모든 요청에 대응?**

- **CSR(Client Side Rendering) 방식으로 요청을 처리**

SSR(Server Side Rendering)

- 기존의 요청방식
- 서버가 사용자의 요청에 적합한 html을 렌더링하여 제공하는 형식
- 전달받은 새 문서를 보여주기 위해 브라우저는 새로고침

![Untitled.png](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled.png)

## CSR(Client Side Rendering)

- 서버로부터 최초로 빈 html 문서를 받아옴
- 각 요청에 대한 대응을 JS를 활용하여 필요한 부분만 다시 렌더링
1. 새로운 페이지를 서버에 AJAX로 요청
2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON방식으로 전달
3. JSON데이터를 JS로 처리 
    
    DOM 트리에 반영(렌더링)
    

![Untitled.png](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%201.png)

### CSR 방식을 사용하는 이유?

1. 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 된다
    
    == 클라이언트 - 서버간 통신 즉, **트래픽의 감소**
    
    == 트래픽의 감소 = **응답속도가 빨라진다**
    
2. 매번 새 문서를 받아 새로고침하는 것이 아니라 **필요한 부분만 고쳐나가므로 각 요청이 끊김없이 진행**
    - SNS에서 추천을 누를 때 마다 첫 페이지로 돌아간다 = 끔찍한 App!
    - 요청이 자연스럽게 진행된다 = UX 향상
3. BE와 FE의 **작업 영역을 명확히 분리** 할 수 있음
    
    = **협업이 용이해짐**
    

### CSR은 만능일까?

- 첫 구동시 필요한 데이터가 많으면 많을수록 최초 작동시작까지 오랜 시간이 소요
- 모바일에 설치된 Web-app을 실행하게 되면 잠깐의 로딩시간이 필요함
- **검색엔진 최적화가 어려움 (SEO Search Engine Optimization)**
    - 서버가 제공하는 것은 HTML
    - 내용을 채우는 것은 AJAX 요청으로 얻는 JSON데이터로 클라이언트가 진행
- 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색엔진에 빈 HTML을 공유하는 SPA서비스가 노출되기는 어려움

### SEO

- 서비스나 제품이 상단에 노출되도록 하는 것 . CSR로는 어려운 것
- 검색엔진 최적화

---

### Vue CDN

```jsx
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
```

### v-model : input에 입력하는 값 화면에 보여주기

- input의 데이터를 message 인 Vue의 data와 양방향 바인딩

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <p id="name">name : {{ message }} </p>
    <input id="inputName" type="text" **v-model="message"**>
  </div>
  
  <script>
    // CODE HERE
    const app = new Vue( // 생성자 함수
    {
      el : '#app',
      data:{
        message:'',

      },
    })
  </script>
</body>
</html>
```

![Untitled](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%202.png)

---

### Vue2 vs Vue3

- 아직 legacy code가 많음
- 상대적으로 문서, 참고자료가 많고 안정적임

---

# Vue instance

## MVVM Pattern

- 소프트웨어 아키텍쳐 패턴의 일종
- 마크업 언어로 구현하는 그래픽 사용자 인터페이스(view)의 개발을 Back-end(model)로 부터 분리시켜 **view가 특정한 모델 플랫폼에 종속되지 않도록 함**

![vue는 view와 model 중개](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%203.png)

vue는 view와 model 중개

- **View** = DOM 우리 눈에 보이는 부분
- **Model** = JSON 실제 데이터
- **View Model**(Vue)
    - View를 위한 모델
    - View와 연결되어(binding) Action을 주고받음
    - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경
    - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩 된 다른 View도 변경된다

### view와 model 이 직접적으로 연결되어있지 않음!

- MVC 패턴에서 Controller를 제외하고 View Model을 넣은 패턴
- View Model을 모르고 Model도 View를 모른다
- View에서 데이터를 변경하면 View Model의 데이터가 변경되고 연관된 다른 View도 함께 변견된다

## 생성자 함수

- 동일한 구조의 객체를 여러개 만들 수 있게 해줌
- 생성자 함수를 사용할 떄는 반드시 new  연산자를 사용
- 함수 이름은 대문자로시작해야함

```
// 1. Vue instance constructor
    const vm = new Vue()
    console.log(vm)
```

### el (element)

- Vue instance와 DOM을 연결(mount) 하는 옵션
    - view와 model을 연결
    - HTML id 혹은 class와 마운트 기능
- Vue instance와 연결되지 않은 DOM 외부는 Vue 영향을 받지 않음
    - Vue 속성 및 메서드 사용 불가

```jsx
// **el**
    const app = new Vue({
      el: '#app', // DOM 연결 
      // **data**
      data: {
        message: 'Hello, Vue!' 
      },
```

- vue 와 연결 된 div에서만 {{message}}를 인스턴스로 받아서 출력함
    - 연결되어있지 않은 div는 {{message}}그대로 출력

### data

- Vue instance의 데이터 객체 혹은 인스턴스 속성
- 데이터 객체는 반드시 기본 객체 {} (Object)여야함
- 객체 내부 아이템들은 value로 모든 타입의 객체를 가질 수 있음
- 정의된 속성은 interpolation {{}} 을 통해 view에 렌더링이 가능함

### method

- Vue instance의 method를 정의하는 곳
- methods 객체 정의
    - 객체 내 print method 정의
    - print method 실행 시 Vue instance> data > message 출력
- method 호출로 data 변경 가능

![Untitled](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%204.png)

```jsx
const vm = new Vue()
    console.log(vm)

    // 2. el
    const app = new Vue({
      el: '#app',
      // 3. data
      data: {
        message: 'Hello, Vue!'
      },

    //   // 4. methods
      methods: {
        print: function () {
          console.log(this.message)
        },
```

![콘솔창에서 app.bye()실행시 DOM에 바로 변경된 결과 반영됨. vue의 강력한 반응성](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%205.png)

콘솔창에서 app.bye()실행시 DOM에 바로 변경된 결과 반영됨. vue의 강력한 반응성

### 메서드를 정의할 때 Arrow Function 사용X

- Arrow Function 사용하면 this가 상위객체(window)를 가리킴
- 호출은 문제가 없으나 this로 vue의 data를 변경하지 못함

---

# Basic of Syntax

## Text interpolation

- RAW HTML
    - v-html directive를 사용하여 data와 바인딩
    - directive : HTML기반 template syntax
    - HTML 기본 속성이 아닌 Vue가 제공하는 특수 속성 값으로 data를 작성

```html
<!-- 1. Text interpolation -->
  <div id="app">
    <p>메시지: {{ msg }}</p>    -->
    <p>HTML 메시지 : {{ rawHTML }}</p>
    <p>HTML 메시지 : <span v-html="rawHTML"></span></p>
    <p>{{ msg.split('').reverse().join('') }}</p>
  </div>

<script>
    // 1. Text interpolation
    const app = new Vue({
      el: '#app',
      data: {
        msg: 'Text interpolation',
        rawHTML: '<span style="color:red"> 빨간 글씨</span>'
      }
    })
</script>
```

![Untitled](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%206.png)

## Directives

- v-접두사가 있는 특수 속성에는 값을 할당할 수 있음
    - 값에는 JS 표현식을 작성할 수 있음
- directive의 역할은 표현식의 값이 변경될 때 **반응적으로  DOM에 적용**하는것

![Untitled](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%207.png)

- `‘:’` 을 통해 전달인자를 받을 수 있음
- `‘.’` 으로 표시되는 특수 접미사 -directive를 특별한 방법으로 바인딩해야함

### v-text

- Text Interpolation과 가장 기본적인 바인딩 방법
- {{ }} 와 유사한 역할

### v-html

- RAW HTML을 표현할 수 있는 방법
- 사용자가 입력하거나 제공하는 컨텐츠에서 절대사용금지

```html
<!-- 2. v-text & v-html -->
  <div id="app2">
    <!-- 2-1. v-text & {{}} -->
    <p v-text="message"></p>
    <!-- 같음 -->
    <p>{{ message }}</p>

    <!-- 2-2. v-html -->
    <p v-html="html"></p>
  </div>
```

```jsx
    const app2 = new Vue({
      el: '#app2',
      data: {
        message: 'Hello!',
        html: '<a href="https://www.google.com">GOOGLE</a>'
      }
    })
```

### v-show

- 표현식에 작성된 값에 따라 element를 보여줄 것인지 결정
    - boolean값이 변경될 때마다 반응
- 대상 element의 display속성을 기본 속상과 none으로 toggle
- 요소 자체는 항상 DOM에 렌더링 됨

### v-if

- isActive값이 변경될 때 반응함
- 값이 false일 경우 DOM에서 사라짐
- v-if v-else-if v-else 형태로 사용

```
<!-- 3. v-show && v-if -->
  <div id="app3">
    <p v-show="isActive">보이니? 안보이니?</p>
    <!-- <p v-if="isActive">안보이니? 보이니?</p> -->
  </div>
```

```jsx

    const app3 = new Vue({
      el: '#app3',
      data: {
        isActive: true
      }
    })
```

![Untitled](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%208.png)

![v-if는 false일 때 아예 사라짐](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%209.png)

v-if는 false일 때 아예 사라짐

### v-show VS v-if

- v-show(Expensive initial load, cheap toggle)
    - 표현식 결과와 관계없이 렌더링 되므로 초기 렌더링 비용이 더 높음
    - display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle비용은 적음
- v-if (Cheap initial load, Expensive toggle)
    - 표현식이 false면 렌더링되지 않기때문에 초기 렌더링 비용이 더 낮음
    - 단, 표현식이 자주 변경되는 경우 잦은 재 렌더링으로 비용증가

### v-for

- String

![Untitled](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%2010.png)

```html
<div v-for="char in myStr">
      {{char}}
    </div>

const app = new Vue({
      el: '#app',
      data: {
        // 1. String
        myStr: 'Hello, World!',
```

![Untitled](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%2011.png)

```html
<div v-for="(char, index) in myStr" :key="index">
      <p>{{ index }}번째 문자열 {{ char }}</p>
    </div>

const app = new Vue({
      el: '#app',
      data: {
        // 1. String
        myStr: 'Hello, World!',
```

- Array

![Untitled](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%2012.png)

```html
<h2>Array</h2>
    <div v-for="(item, index) in myArr" :key="index">
      <p>{{ index }}번째 아이템 {{ item }}</p>
    </div>

    <div v-for="(item, index) in myArr2" :key="`arry-${index}`">
      <p>{{ index }}번째 아이템</p>
		  <p>{{ item.name }}</p>
    </div>
```

```jsx
// 2-1. Array
        myArr: ['python', 'django', 'vue.js'],

        // 2-2. Array with Object
        myArr2: [
          { id: 1, name: 'python', completed: true},
          { id: 2, name: 'django', completed: true},
          { id: 3, name: 'vue.js', completed: false},
			  ],
```

- Object

```html
<h2>Object</h2>
    <div v-for="value in myObj">
      <p>{{ value }}</p>
    </div>

    <div v-for="(value, key) in myObj"  :key="key">
      <p>{{ key }} : {{ value }}</p>
    </div>
```

```jsx
// 3. Object
        myObj: {
          name: 'harry',
          age: 27
        },
```

![Untitled](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%2013.png)

### v-for 사용시 반드시 key속성값을 각 요소에 작성

- 주로 v-for directive 작성 시 사용
- vue 화면 구성 시 이전과 달라진 점을 확인하는 용도로 사용
    - 따라서 key가 중복되어서는 안된다
- 각 요소가 고유한 값을 가지고 있지 않다면 생략가능
- 각각의 v-for가 올바르게 동작하게 하기 위함. 에러를 발생시킬 수 있음
- 배열은 보통 문자열+인덱스

### v-on

- addEventListener의 첫 번쨰 인자와 동일한 값들로 구성
- method를 통한 data 조작도 가능
- method에 인자를 넘기는 방법은 일반함수를 호출할 때와 동일한 방식
- `‘:'` 을통해 전달된 인자에따라 특별한 modifiers(수식어)가 있을 수 있음
- `‘@’` shortcut제공

```html
<button v-on:click="number++">increase Number</button>
    <p>{{ number }}</p>
```

```jsx
<script>
    const app = new Vue({
      el: '#app',
      data: {
        number: 0,
        isActive: false,
      },
```

- 메서드 호출

```html
<button v-on:click="toggleActive">toggle isActive</button>
    <p>{{ isActive }}</p>
```

```html
<button @click="checkActive(isActive)">check isActive</button>
```

```jsx
methods: {
        toggleActive: function () {
          this.isActive = !this.isActive
        },
```

### v-bind

- HTML 의 속성값에 JS를 사용하기위한 라이브러리

> html의 속성값을 변수로 받아와 사용
> 

```html
<a v-bind:href="url">Go To GOOGLE</a>
```

```jsx
const app2 = new Vue({
      el: '#app2',
      data: {
       url: 'https://www.google.com/',
```

> class 명을 변수로 받아와 사용
> 

```jsx
<p v-bind:class="redTextClass">빨간 글씨</p>
<p v-bind:class="{ 'red-text': true }">빨간 글씨</p>
<p v-bind:class="[redTextClass, borderBlack]">빨간 글씨, 검은 테두리</p>
```

```jsx
const app2 = new Vue({
      el: '#app2',
      data: {
        redTextClass: 'red-text',
        borderBlack: 'border-black',
```

> 상황에따른 활성화
> 

```html
<p :class="theme">상황에 따른 활성화</p>
<button @click="darkModeToggle">dark Mode {{ isActive }}</button>
```

```jsx
methods: {
        darkModeToggle() {
          this.isActive = !this.isActive
          if (this.isActive) {
            this.theme = 'dark-mode'
          } else {
            this.theme = 'white-mode'
          }
        }
      }
```

![Untitled](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%2014.png)

![Untitled](Vue%20Basic%20e798ad575a4d4fc08d1526b4ac15ad98/Untitled%2015.png)

### V-model

- Vue instance와 DOM의 양방향 바인딩!
- v-model로는 조합형 문자를 사용할 수 없어서 `@input=”메소드명.”` 형태로 사용해야한다

```html
<body>
  <div id="app">
    <h2>1. Input -> Data</h2>
    <h3>{{ myMessage }}</h3>
    <input @input="onInputChange" type="text">
    <hr>

    <h2>2. Input <-> Data</h2>
    <h3>{{ myMessage2 }}</h3>
    <input v-model="myMessage2" type="text">
    <hr>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        myMessage: '',
        myMessage2: '',
      },
      methods: {
        onInputChange: function (event) {
          this.myMessage = event.target.value
        },
      }
    })
  </script>
```

---

## Vue advanced

### computed

- Vue in stance가 가진 optinos중 하나
- computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산
    - 계산 결과가 변하기 전까지 함수를 재호출 하는 것이 아닌 계산된 값을 반환
    - 메서드는 사용할 때마다 계산함
- 재계산이 적은 것을  computed로 주로 사용

```html
<body>
  <div id="app">
    <h1>data_01 : {{ number1 }}</h1>
    <h1>data_02 : {{ number2 }}</h1>
    <hr>
    <h1>add_method : {{ add_method() }}</h1>
    <h1>add_method : {{ add_method() }}</h1>
    <h1>add_method : {{ add_method() }}</h1>
    <hr>
    <h1>add_computed : {{ add_computed }}</h1>
    <h1>add_computed : {{ add_computed }}</h1>
    <h1>add_computed : {{ add_computed }}</h1>
    <hr>
    <button v-on:click="dataChange">Change Data</button>
  </div>
```

```jsx
const app = new Vue({
      el: '#app',
      data: {
        number1: 100,
        number2: 100
      },
      computed: {
        add_computed: function () {
          console.log('computed 실행됨!')
          return this.number1 + this.number2
        }
      },
      methods: {
        add_method: function () {
          console.log('method 실행됨!')
          return this.number1 + this.number2
        },
        dataChange: function () {
          this.number1 = 200
          this.number2 = 300
        }
      }
    
```

## watch

- 특정 데이터의 변화를 감지하는 기능
    - 감시 대상이 변화가 있으면 작동
    - watch 객체를 정의
    - 감시할 대상 data를 지정
    - data가 변할 시 실행 할 함수를 정의
- watch: { number : function(val, oldVal) }.
    - val 현재값
    - oldVal 과거값
- 디버깅용으로 많이 쓰인다

```jsx
watch: {
        number: function (val, oldVal) {
          console.log(val, oldVal)
        },
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <h3>Increase number</h3>
    <p>{{ number }}</p>
    <button @click="number++">+</button>
    <hr>

    <h3>Change name</h3>
    <p>{{ name }}</p>
    <input type="text" v-model="name">
    <hr>

    <h3>push myObj</h3>
    <p>{{ myObj }}</p>
    <button @click="itemChange">change Item</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        number: 0,
        name: '',
        myObj: {completed: true}
      },
      methods: {
        nameChange: function () {
          console.log('name is changed')
        },

        itemChange: function () {
          this.myObj.completed = !this.myObj.completed
        }
      },
      watch: {
        number: function (val, oldVal) {
          console.log(val, oldVal)
        },

        name: {
          handler: 'nameChange'
        },

        myObj: {
          handler: function (val) { // 메소드에는 handler 사용
            console.log(val)
          },
          deep: true // 
        },
      }
    })
  </script>
</body>
</html>
```

## filter

- 텍스트 형식화를 적용할 수 있는 필터
- - interpolation 혹은 v-bind를 사용할 때
- 필터는 체이닝이 가능하다

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <p>{{ numbers }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      },
      filters: {
        getOddNums: function (nums) {
          const oddNums = nums.filter((num) => {
            return num % 2
          })
          return oddNums
        },
        
        getUnderTenNums: function (nums) {
          const underTen = nums.filter((num) => {
            return num < 10
          })
          return underTen
        }
      }
    })
  </script>
</body>
</html>
```

---

## Vue Style Guide

### v-if 와 v-for를 같이 사용하지 않기

- v-if가 먼저 계산되고 해당 처리 시점에 반복 변수인 user가 존재하지 않기 때문에 에러 발생 (2 버전에서는 v-for가 더 높은 우선순위를 가진다)
- Vue가 디렉티브 처리할 때 v-if가 v-for보다 높은 우선순위를 가진다
- 동시에 사용해야한다면
    - 목록의 항목을 필터링 할 경우 activeUsers 로 대체
    
    ```jsx
    <ul>
      <li
        v-for="user in activeUsers"
        :key="user.id"
      >
        {{ user.name }}
      </li>
    </ul>
    ```
    
    - 숨김 목록의 렌더링을 피할때 v-if를 컨테이너 엘리먼트로 옮긴다.
    
    ```jsx
    <ul>
      <template v-for="user in users" :key="user.id">
        <li v-if="user.isActive">
          {{ user.name }}
        </li>
      </template>
    </ul>
    ```
    

---

### lodash cdn

```jsx
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
```

### Lodash 사용해서 랜덤한 값 표출하기

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <h2>점메추</h2>
    <!-- <p> 메뉴 : {{ lunch }}</p> -->
    <button v-on:click="selectOne">"Pick One</button>
    <p> 점심에는 {{ selectedLunch }} EZ</p>
    <hr>
    <h2>lotto</h2>
    <button @click="selectNumber">Pick Numbers</button>
    <p> 오늘의 당첨 번호 {{selectedNumbers}} 입니다</p>
  </div>

  <hr>
  <!-- view를 쓰겠다! cdn -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <!-- lodash를 쓰겠다 cdn -->
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    const app = new Vue({
      el : '#app',
      data :{
        lunch : ['시래기 비빔밥', '볶음밥자장면', '너구리'],
        selectedLunch: null,
        selectedNumbers: []
      },
      methods: {
        // arrow function 을 쓰면 this를 못씀. window를 가르키게 되니까 주의
        selectOne: function() {
          console.log(_.random(0,this.lunch.length-1))
          let idx = _.random(0, this.lunch.length-1)
          this.selectedLunch = this.lunch[idx]
        },
        // 함수 정의 아래처럼 할 수도
        selectNumber(){
          const numbers = _.range(1, 46)
          this.selectedNumbers = _.sampleSize(numbers, 6)
        }
      }
    })
  </script>
</body>
</html>
```