# Vuex

- 목차

## 상태 관리 State Management

### State

- 현재에 대한 정보
- Web application에서 상태는 Data
- 각 component는 독립적이고 각각의 상태(data)를 가지는데
- 이러한 component들이 모여 하나의 App을 구성
    
    ⇒ 여러개의 component가 같은 상태를 유지할 필요가 있음
    
    ⇒ 이것이 상태관리의 필요성
    

### Props 와 Emit을 통한 상태관리

- 같은 데이터를 공유하므로 각 컴포넌트가 동일한 상태를 유지하고있음
- 데이터의 흐름을 직관적으로 파악 가능
- **BUT 중첩이 깊어지면**
    - 데이터의 전달이 쉽지않다
    - component가 많아지면 데이터 전달 구조가 복잡해짐
    - 유지보수 비용이 높아진다

### 중앙 저장소 Centrailized Store

- 중앙 저장소에 데이터를 모아서 상태를 관리하는 것 === Vuex
- component 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경할 수 있음
- 중앙 저장소의 데이터가 변경되면 각각의 컴포넌트는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영
- 규모가 크거나 컴포넌트 중첩이 깉은 프로젝트의 관리가 편리

---

## Vuex

- state management pattern + Library for vue.js
- 중앙 저장소를 통해 상태관리를 할 수 있도록 하는 라이브러리
- 데이터가 예측 가능한 방식으로만 변경될 수 있도록하는 규칙을 설정하며  Vue의 반응성을 효율적으로 사용하는 상태관리기능을 제공
- Vue의 공식 도구로서 다양한 기능을 제공
- 

![Untitled](Vuex%204b92e626091f438f89fe7ead2e5d1654/Untitled.png)

### vuex 시작하기

```bash
vue create vuex-app
cd vuex-app
**vue add vuex # vuex/src/store 새로운 중앙 저장소 폴더가 생긴 것을 확인**
```

### vuex 보관소 구조

- vuex 설치시 store 폴더 안에 자동 생성되는 파일 구조는 아래와 같다

```bash
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
```

- vue와 비교

```jsx
export default new Vuex.Store({
	name: 'VueInstance',
  data: function(){
		return{
		}
  },
  computed: {
  },
  methods: {
  },
})
```

![Untitled](Vuex%204b92e626091f438f89fe7ead2e5d1654/Untitled%201.png)

### state

- vue 인스턴스의 data
- 중앙에서 관리하는 모든 상태정보
- state의 데이터가 변화하면 해당 데이터를 사용하는 컴포넌트도 자동으로 다시 렌더링
- `$store.state` 로 state 데이터에 접근

### Mutations

- 실제로 **state를 변경하는 유일한 메서드**
- vue 인스턴스의 methods
    - **Mutations에서 호출되는 핸들러함수는 반드시 동기적이어야함**
    - 비동기 로직으로 state를 변경하는 경우 변경 시기를 특정할 수 없기 때문에 mutation에서 비동기로직 사용x
    - 첫번째 인자로 state를 받으며 component 혹은 Actions에서 **commit()메서드로** 호출된다
- mutation, action 에서 호출되는 함수를 handler라고 한다

### Actions

- mutations과 유사하지만 **비동기 작업 포함 가능**
- **state를 직접 변경하지 않고 commit()메서드로 mutations를 호출해서 state를 변경**
- context 객체를 인자로 받으며 이 객체를 통해 store.js의 **모든 요소와 메서드에 접근할 수 있음**( == 즉 직접 변경할 수 있지만 하지 않아야함!)
- component에서 dispatch() 메서드에 의해 호출된다
- mutations는 한가지 일 만 하고 나머지는 actions가 함

### Mutations & Actions

- 둘다 메서드
- Mutations : state를 변경
- Actions : state를 변경을 제외한 나머지 로직

![Untitled](Vuex%204b92e626091f438f89fe7ead2e5d1654/Untitled%202.png)

### Getters

- vue 인스턴스의 computed에 해당
- **state를 활용하여 계산된 값을 얻고자 할 때 사용**
    - 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
- computed와 마찬가지로 getters의 경과는 캐시되며 종속된 값이 변경된 경우에만 재계산된다
- getters에서 계산된 값은 state에 영향을 미치지 않음
- 첫번째 인자로 state , 두번째 인자로 getter를 받음
- state를 활용해 계산한 새로운 변수값

![코드 작성 순서! ](Vuex%204b92e626091f438f89fe7ead2e5d1654/Untitled%203.png)

코드 작성 순서! 

---

## Vuex 실습

### * 객체 메서드 축약형

- `:` 과 `function 키워드` 없이 사용

```jsx
const Obj2 = {
	addValue(value) { return value },
}
```

```jsx
const Obj2 = {
	addValue : function (value) { return value },
}
```

1. 중앙 저장소 메세지 생성
    
    ```jsx
    state: {
        message : 'message in store'
      },
    ```
    
    - html에서 직접 접근
    
    template에서 $store.state로 바로 접근
    
    ```jsx
    <template>
      <div id="app">
        <h1>{{ $store.state.message }}</h1>
      </div>
    </template>
    ```
    
    ![Untitled](Vuex%204b92e626091f438f89fe7ead2e5d1654/Untitled%204.png)
    
    - script를 통해 computed에 정의 후 접근**(권장)**
    
    ```jsx
    <h1>{{ message }}</h1>
    ```
    
    ```jsx
    computed: {
        message(){
          return this.$store.state.message
        }
      }
    ```
    
2. actions에서 state를 변경할 수 있는 mutations를 호출
    
    이 actions은 dispatch()에 의해 호출
    
    - 사용자 입력값을 data에 저장하고 store에 있는 message의 값에 data에 저장한 값 저장하기 (status 변경)
    
    ```jsx
    <div id="app">
        <h1>{{ message }}</h1>
        <input 
          type="text"
          @keyup.enter="changeMessage"
          v-model="inputData"
          >
      </div>
    ```
    
    ```jsx
    data(){
        return{
          inputData: null,
        }
      },
    computed: {
        message(){
          return this.$store.state.message
        }
      },
      methods: {
        changeMessage(){
          const newMessage = this.inputData
          // action 호출
          // this.$store.dispatch('액션 메서드 이름', 추가데이터)
          this.$store.dispatch('changeMessageAction',newMessage)
        }
      }
    ```
    
    - actions에서 메세지를 전달받는다
        - store의 모든 속성을 포함하는 context 객체를 전달받는것이 actions의 특징
        - 하지만 actions에서 state를 직접 조작하는 것은 삼가야함
        - 두번째 인자가 payload ⇒ 넘겨준 데이터를 받아서 사용
    
    ```jsx
    actions: {
        // store의 모든 속성을 포함하는 context 객체를 전달받는것이 actions의 특징 
        changeMessageAction(context, newMessage){
          console.log(context)
          console.log(newMessage)
        }
      },
    ```
    
    ![actions에서 받은 context 값이 store의 모든 데이터! 
    그리고 전달받은 메세지](Vuex%204b92e626091f438f89fe7ead2e5d1654/Untitled%205.png)
    
    actions에서 받은 context 값이 store의 모든 데이터! 
    그리고 전달받은 메세지
    
    - commit()으로 mutations호출
    
    ```jsx
    mutations: {
        // mutations 라는 것을 강조하기 위해 , actions와 구분하기 위해 상수 표기하듯이 함
        CHANGE_MESSAGE(state, newMessage){
          console.log(state)
          console.log(newMessage)
          state.message = newMessage
        }
      },
      actions: {
        changeMessageAction(context, newMessage){
          context.commit('CHANGE_MESSAGE', newMessage)
        }
      },
    ```
    
    ![mutations에서 받은 state와 데이터](Vuex%204b92e626091f438f89fe7ead2e5d1654/Untitled%206.png)
    
    mutations에서 받은 state와 데이터
    

1. getters (state를 활용한 새로운 변수)
    
    ```jsx
    getters: {
        messageLength(state){
          return state.message.length
        }
      },
    ```
    
    - getters는 계산된 값이기때문에 computed에서 사용한다
    
    ```jsx
    computed: {
        message(){
          ...
        messageLength(){
          return this.$store.getters.messageLength
        }
      },
    ```
    
    - template에서
    
    ```jsx
    <h3>입력된 문자의 길이는 {{messageLength}}</h3>
    ```
    
2. 

---

## Lifecycle Hooks

- 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
    - Vue 인스턴스가 생성된 경우
    - 인스턴스를 DOM에 마운트 하는 경우
    - 데이터가 변경되어 DOM을 업데이트하는 경우 등
- 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음
- 이를 Lifecycle Hooks라고 함

![빨간 버튼 부분이 우리가 코드를 넣을 수 있는 부분](Vuex%204b92e626091f438f89fe7ead2e5d1654/Untitled%207.png)

빨간 버튼 부분이 우리가 코드를 넣을 수 있는 부분

- created
    - data, computed 등의 설정이 완료된 상태
    - **Vue instance가 생성된 직후 호출**된다
    - 서버에서 받은 데이터를 vue instance의 data에 할당하는 로직을 구현하기 적합
    - 단 **mount되지 않아 DOM 요소에 접근할 수 없음**
    - 버튼을 누르지 않고 첫 실행 시 특정 함수를 실행 하고싶다면 **created 함수에 해당 함수를 추가**
        
        ```jsx
        created(){
            this.getDogImage()
          }
        ```
        
- mounted
    - vue 인스턴스가 생성된 이후
    - mounted 시점에서는 DOM 조작이 가능하다
    
    ```jsx
    mounted() {
        const button = document.querySelector('button')
        button.innerText = '멍멍!'
      }
    ```
    
    - created 시점에서 button 을 select 하려하면 에러가 발생한다 ⇒ DOM 이 생성되지 않았기 때문에(mount이전) button을 선택할 수 없음
- updated
    - 데이터가 변경되어 DOM이 새로 그려지는 시점
    
    ```jsx
    updated() {
        console.log('새로운 멍멍이')
      }
    ```
    

### instance 각각의 Lifecycle이 서로 영향을 줄까??

- 부모 컴포넌트의 mounted hook 이 실행되었다고해서 자식이  mount된 것이 아니고
- 부모 컴포넌트가 updated hook 이 실행되었다고 해서 자식이 updated 된 것이 아님
    - 부착 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않은 것
- instance마다 각각의 lifecycle을 가지고 있기 때문!