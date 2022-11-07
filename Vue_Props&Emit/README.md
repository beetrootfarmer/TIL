# Pass Props & Emit Event

### node module 생성

```jsx
npm install
```

---

# Data in Components

> 한 페이지 내에서 데이터를 공유하려면 어떻게 해야하나??
> 

⇒ 뷰에서는 부모-자식 관계에서만 데이터를 주고받게 함

⇒ 데이터의 흐름을 파악하기 용이하기 때문에 유지보수가 쉬워짐

> Pass Props & Emit Event
> 
- **Pass Props** : 부모 ⇒ 자식 으로의 데이터 흐름
- **Emit Event** : 자식 ⇒ 부모로의 데이터 흐름

## Pass Props

- **요소의 속성을 사용해 데이터를 전달**
- props는 부모 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 자식 컴포넌트는 **props 옵션**을 사용하여 수신하는 **props를 명시적으로 선언**해야함

- **static props**
- 부모측에서 자식 컴포넌트를 불러올 때 msg 속성으로 전달하고 자식 컴포넌트에서 {{ }} 형태로 사용하는 것을 확인 할 수 있음
- kebab-case 형태로 작성해야함 (html에서 대소문자 구문 못함)
    - *보낼때는 케밥  받을때는 카멜* (template에서 보내고 script에서 받음) *케밥먹은 낙타 바이 MC 하림!!*
    - map-title ⇒ mapTitle
- 데이터를 받는 하위컴포넌트에서도 props에 대해 명시적으로 작성해야함
- `prop-data-name=”value”`

```jsx
<HelloWorld msg="Welcome to Your Vue.js App"/>
```

```jsx
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
...
<script>
...
	props:{
		msg : String
	}
}
```

- **Dynamic props**
- 변수를 props로
- v-bind directive를 사용해 데이터를 동적으로 바인딩
- 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트된다
- **vue cli에서는 data가 함수의 return 객체여야한다💫💫**
    - 각 Vue 인스턴스는 같은 data 객체를 공유하므로 새로운 data 객체를 반환(return)하여 사용
    - data가 여러개일 때 key값을 분리하기 위해서 component단위 구조에서는 data를 return객체로 사용!
    
    ```jsx
    <MyComponentItem2 :dynamic-props="dynamicProps"/>   // html
    ...
    data:function() {                                   // scripts
        return {
          dynamicProps: '이것은 DYNAMIC DATA',
        }
      }
    ```
    
    ```jsx
    <p>{{ dynamicProps }}</p>                          // html
    ...
    props : {                                          // scripts
        dynamicProps: String,
      }
    ```
    
- v-bind로 묶여있는 “ “ 안의 구문은 javascript구문
    - 따라서 dynamicProps라는 변수에 대한 data를 전달할 수 있는 것
    - 숫자를 전달하기위한 방법
    
    ```jsx
    // string "1"을 전달 - static props
    <SomeComponent num-props="1"/>
    
    // JS 표현식이 들어가서 숫자 1을 전달 - dynamic props
    <SomeComponent :num-props="1"/>
    ```
    

- **단방향 데이터의 흐름**
- 모든 props는 부모에서 자식으로 즉 아래로 단방향 바인딩을 형성
- 부모 속성이 업데이트되면 자식으로 흐르지만 반대방향을 아님
    - 부모컴포넌트가 업데이트되면 자식 컴포넌트들의 모든 prop들이 새로고침된다

⇒ 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경해 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지

⇒ 하위 컴포넌트에서 prop 변경 시도하면 Vue에서 경고를 출력함

## Emit Event

- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 이벤트를 발생시킴
    1. 데이터를 이벤트 리스너의 콜백함수의 인자로 전달
    2. 상위 컴포넌트는 이벤트를 통해 인자를 받음

![Untitled](Pass%20Props%20&%20Emit%20Event%2030f9b2d2fb7d403bbae8315d576658bc/Untitled.png)

```jsx
<button @click="childToParent">소리쳐! 다같이 소리쳐! 쓰려질 순 없잖아 베이베!</button>
...
methods: {
    childToParent: function(){
      this.$emit('zing-zing', '두번째 인자는 데이터') // 부모 컴포넌트에 소리치는 부분
    }
  },
```

```jsx
<MyComponentItem2 static-props="MC에서 보낸 데이터" 
  :dynamic-props="dynamicProps"
  @zing-zing="parentGetEvent"        // 부모 컴포넌트에서 듣고 본인만의 메서드를 호출하는 부분
  />
...
methods:{
    parentGetEvent:function(childSays){
      console.log(childSays)             // '두번째 인자는 데이터'
    }
  }
```

- $emit(’event-name’) 형식으로 부모컴포넌트에 이벤트가 발생했다는 것을 알림
- 한 단계씩만 위로 올라갈 수 있다(like 봉화 🔥)
- 이렇게 전달한 데이터는 이벤트와 연결된 부모 컴포넌트의 핸들러 함수의 인자로 사용 가능

- 동적인 데이터 올리기

```jsx
<input 
      type="text" 
      v-model="childInputData"
      @keyup="ChildInput"
      placeholder="동적인 데이터">
...
data: function() {
    return {
      childInputData: null,
    }
  },
methods: {
    ChildInput: function name() {
      this.$emit('child-input', this.childInputData)
    }
  },
```

```jsx
<MyComponentItem2 static-props="MC에서 보낸 데이터" 
  @child-input="getDynamicData"
/>
...
methods:{
    getDynamicData: function(childSayss){
      console.log(`방금 뭐라고? ${childSayss}`)
    }
```

![emit event 발생 확인하는 방법 : Timeline에 Component Evnet](Pass%20Props%20&%20Emit%20Event%2030f9b2d2fb7d403bbae8315d576658bc/Untitled%201.png)

emit event 발생 확인하는 방법 : Timeline에 Component Evnet

![Untitled](Pass%20Props%20&%20Emit%20Event%2030f9b2d2fb7d403bbae8315d576658bc/Untitled%202.png)

![Untitled](Pass%20Props%20&%20Emit%20Event%2030f9b2d2fb7d403bbae8315d576658bc/Untitled%203.png)