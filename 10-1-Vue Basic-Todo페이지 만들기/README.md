# Vue Basic : Todo 페이지 만들기

### Vue CDN

```jsx
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
```

### 할일 입력할 input, button만들기

```html
<input @keyup.enter="addTodo" type="text" v-model="content">
<button @click="addTodo">+</button>
```

- `@click="addTodo"` : v-on 으로 click listener 설정. 버튼 클릭 시addTodo method실행되도록
- `@keyup.enter="addTodo"` : v-on으로 enter keyup 발생시 addTodo method실행
- `v-model="content"` : content 라는 데이터와 html element인 input을 양방향 바인딩

### Vue 생성자 data에 todos 리스트 생성

```jsx
const app = new Vue({
      el:'#app',
      data:{
        status: 'all',
        content : null, //input tag의 v-model을 통해 input값과 연결이 된 부분
        todos : []
      },
    })
```

- `todos : []` : todo 값을 넣어줄 빈 배열 데이터

### input 태그 값을 content로 받아서 todos 리스트에 넣는 addTodo() 메소드 생성

```jsx
methods:{
        addTodo(){
          const todo ={
            content:this.content,
            isCompleted:false,
            data: new Date().getTime()
          }
          this.todos.push(todo) // todo 객체를 만들고 todos에 push
          this.content = null // input에 들어가있던 값을 지워주는 부분
        },
			}
```

- `const todo ={
  content : this.content,
  isCompleted : false,
  data : new Date().getTime()
 }` : input으로 받은 content를 가지는 todo 객체를 만든다
- `this.todos.push(todo)` : todos[]에 담아준다
- 리스트에 담고 content(input 값) null로 초기화

### todos를 li 태그에 v-for 옵션을 사용해서 표출 (key값은 생성날짜로 바인딩)

```html
<ul>
      <li v-for="todo in todos" :key="todo.date"> <!-- ':' v-bind shorcut 으로 각각의 객체들을 date key값으로 바인딩-->
        <!-- 3. 완료 여부 변경 가능한 checkbox -->
        <!-- 양방향이라는것! todo 의 isCompleted 값이 바뀌면 체크 상태가 바뀐다
              체크 상태가 바뀌면 isCompleted 값이 바뀐다  -->
        <input 
          type="checkbox"
          v-model="todo.isCompleted"
        >
        <span
          :class="{ completed : todo.isCompleted, 'none' : !todo.isCompleted}"
        >{{ todo.content }}</span> 
        <!-- class는 애초에 그런식으로 특정상황에서 넣고빼고 하는게 자주 있다보니까 class에 바인딩 시 조건문을 쓸 수 있는 기능을 만들어놨다 -->
      </li>
    </ul>
```

- `<li v-for="todo in todos" :key="todo.date">` : v-for 옵션으로 todos 를 순회하며 li 태그로 표출. key값은 생성날짜
    - ':' v-bind shorcut 으로 각각의 객체들을 date key값으로 바인딩
- `<input 
   type="checkbox"
   v-model="todo.isCompleted"
>` : v-model로 todo의 isCompleted 옵션과 양방향 바인딩
    - `@click="isCompletedToggle(todo)"` 의 형태로 써서 체크 할 경우 속성값을 바꾸는 함수를 사용하는 방법도 있음
        
        ```
        isCompletedToggle(todo){
                  todo.isCompleted = !todo.isCompleted
                },
        ```
        
- 조건문을 사용한 **class 조건 binding**
    
    ```jsx
    조건 바인딩 {클래스명:표현식}
    ```
    
    쉼표로 구분해서 **다중 binding**을 할 수 있다
    
    ```jsx
    :class ="{ completed : todo.isCompleted, none : !todo.isCompleted}"
    ```
    

### checkbox를 todo.isCompleted 속성과 v-model 연결

```jsx
 <input 
    type="checkbox"
    v-model="todo.isCompleted"
 >
```

### todo의 isCompleted를 filter해서 삭제하는 deleteCompleted()메소드 생성

```jsx
<button @click="deleteCompleted">완료된 할 일 지우기</button>
```

```jsx
methods:{
        addTodo(){
          const todo ={
            content:this.content,
            isCompleted:false,
            data: new Date().getTime()
          }
          this.todos.push(todo) // todo 객체를 만들고 todos에 push
          this.content = null // input에 들어가있던 값을 지워주는 부분
        },
        isCompletedToggle(todo){
          todo.isCompleted = !todo.isCompleted
        },
        deleteCompleted(){
          //반환값이 true인 객체들만 모아서 새 배열을 return
          // this.todos = this.todos.filter(function(todo){
          //   return !todo.isCompleted
          // })
          // arrow function 쓸거임. method 정의하는 경우가 아니기때문에 괜찮음
          this.todo = this.todos.filter(todo => !todo.isCompleted)
        }
      },
```

- !todo.isComplete인(완료되지 않은) todo를 filter해서 this.todo에 재정의하는 함수
- method가 아니기때문에 화살표 함수 사용이 가능하다

### select tag의 값이 바뀌면 todos 리스트 새로 보여주는 todoListByStatus() 메소드 생성

```html
<select v-model="status" >  
      <option value="all">전체</option>
      <option value="inProgress">진행중</option>
      <option value="completed">완료</option>
    </select>
```

![항상 사용할 Vue 구조임](Vue%20Basic%20Todo%20%E1%84%91%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%8C%E1%85%B5%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5%20dffa24b257404c8ebbde39b19a9216f3/Untitled.png)

항상 사용할 Vue 구조임

```jsx
computed : {
        todoListByStatus(){
          return this.todos.filter(todo => {
            if (this.status === 'inProgress'){
              return todo.isCompleted === false
              // return !todo.isCompleted //완료가 안된 애들만 모아서 반환
            }
            if (this.status === 'completed'){
              return todo.isCompleted
            }
            return true 
            // 앞의 if문에 걸리지 않은것(all)은 filter 모두 true 반환해서 모든 객체를 그대로 가진 것을 반환 
          })
        }
      }
```

❗ **computed 메소드 호출 방법?**

li 순회할 때 사용가능

```jsx
<li v-for="todo in todoListByStatus" :key="todo.date">
```