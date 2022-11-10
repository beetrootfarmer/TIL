# Vue Routing

# Routing

- 네트워크 경로를 선택하는 프로세스
- 웹 서비스에서의 라우팅
    - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것

## Routing in SSR

- Server가 모든 라우팅을 통제
- URL 요청이 들어오면 응답으로 완성된 HTML 제공
    - 장고로 보낸 요청의 응답 HTML은 완성본 상태
- 결론적으로 Routing(URL)에 대한 결정권을 서버가 가진다

## Routing in SPA/ CSR

- 서버는 하나의 HTML을 제공하고 이후 모든 동작은 JavaScript코드를 활용
    - DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios같은 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
- 즉 하나의 URL만을 가진다

## 왜 routing

- 반드시 URL이 바뀌어야하나? 유저의 사용성 관점에서 필요
- routing이 없다면
    - 유저가 페이지 변화를 감지할 수 없음
    - 페이지가 무엇을 렌더링 중인지 상태를 알 수 X
        - 새로고침 시 처음 페이지로 돌아감
        - 링크 공유시 처음 페이지만 공유 가능
    - 뒤로가기 불가능

---

# Vue Router

- vue의 공식 라우터
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- 라우트(routes)에 컴포넌트를 매핑한 후 어떤 URL에서 렌더링할지 알려줌
    - 즉 SPA를 MPA처럼 URL을 이동하면서 사용 가능
    - SPA의 단점 중 하나인 URL이 변경되지 않는다를 해결
- MPA(Multiple Page Application)
    - 여러개의 페이지로 구성된 애플리케이션
    - SSR방식으로 렌더링

## Vue Router 시작하기

- CLI를 통해 router plugin 적용
    
    `vue create vue-router-app`
    
    `cd vue-router-app`
    
    `vue add router`
    
    - User history mode for router ? → Y
    - **history mode**
        - **브라우저의 History API를 활용한 방식으로**
        - **새로고침 없이 URL이동기록을 남길 수 있음**
        - **history mode를 설정하지 않으면 #hash mode로 설정된다**
- 바뀐 폴더구조

![Untitled](Vue%20Routing%2031712167f3464d519acb03849e3adaf4/Untitled.png)

![Untitled](Vue%20Routing%2031712167f3464d519acb03849e3adaf4/Untitled%201.png)

![컴포넌트에 따른 url mapping](Vue%20Routing%2031712167f3464d519acb03849e3adaf4/Untitled%202.png)

컴포넌트에 따른 url mapping

### router-link

- a태그의 역할 → url 이동
- routes에 등록된 컴포넌트와 매핑된다
- 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
- 목표 경로는 `to` 속성으로 지정된다
- 기능에 맞게 html에서 a태그로 rendering되지만 필요에 따라 다른 태그로 바꿀 수 있음

### router-view

- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미한다
- router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
- Django의 block tag와 비슷함
    - App.vue는 base.html의 역할
    - router-view는 block 태그로 감싼 부분

## src/router/index.js

- 라우터에 관련된 정보 및 설정이 작성되는 곳
- Django에서의 urls.py
- routes에 URL와 컴포넌트를 매핑

```python
const routes = [
	{
		path: '/',
		name: 'home',
		component: HomeView
	},
],
```

```python
urlpatterns = [
	path('', views.home, name='home'),
```

### src/Views

- router-view에 들어갈 component 작성
- 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나눠짐
- 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
- views/
    - routes에 매핑되는 컴포넌트
    - 즉 <router-view>의 위치에 렌더링되는 컴포넌트를 모아두는 폴더
    - 다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것을 권장
        - App 컴포넌트 내부의 AboutView & HomeView 컴포넌트
- components/
    - routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더
        - HomeView컴포넌트 내부의 HelloWorld 컴포넌트
        - View로 끝나도록 만드는 것을 권장

---

## Vue Router로 주소를 이동하는 2가지 방법

### 1. 선언적 방식 네비게이션

- router-link의 `to` 속성으로 주소를 전달
    - routers에 등록된 주소와 매핑된 컴포넌트로 이동(name 설정 값)
    - 장고의 path함수의 name인자 활용과 같은 방식!
    
    ```python
    <router-link to="/about"> About </router-link>
    ===
    <router-link :to="{ name : about }"> About </router-link>  // v-bind를 사용해서 이름으로 연결
    ```
    

### 2. 프로그래밍 방식 네비게이션

- Vue인스턴스 내부에서 라우터 인스턴스에 `$router` 로 접근할 수 있음
- 다른 URL로 이동하려면 `this.$router.push`
    - history stack에 이동할 URL을 넣는(push) 방식
    - history stack에 기록이 남기때문에 사용자가 브라우저의 뒤로가기 버튼을 클릭하면 이전 URL로 이동할 수 있음
- 결국 `<router-link :to="...">` 를 클릭하는 것과 `$router.push` 를 호출하는 것은 같은 동작임
    
    ```python
    <template>
      <div class="about">
        <h1>This is an about page</h1>
        <router-link :to="{ name: 'home' }">홈으로!</router-link>
        <button @click="toHome">집으로!</button>
      </div>
    </template>
    <script>
    export default {
      name: 'AboutView',
      methods:{
        toHome(){
          this.$router.push({ name: 'home' })
        }
      }
    }
    </script>
    ```
    

---

## Dynamic Route Matching

- 동적 인자 전달
- URL의 특정 값을 변수처럼 사용할 수 있음 (장고에서 variable routing)
1. 라우터 만들기
    
    ```python
    import HomeView from '@/views/HomeView.vue'
    ...
    {
        path: '/hello/:userName',
        name: 'hello',
        component: () => import('../views/HelloView.vue')
      }
    ```
    
2. 라우터에 직접 연결되는 HelloView.vue는 views 폴더에 생성
    
    ```python
    <template>
      <div class="hello">
        <h1>Hello, {{ $route.params.userName}} </h1>
      </div>
    </template>
    ```
    
3. 2를 vue스럽게 만들기
    
    ```python
    <template>
      <div class="hello">
        <h1>Hello, {{userName}} </h1>
      </div>
    </template>
    
    <script>
    export default {
      name: 'HelloView',
      data(){
        return {
          userName : this.$route.params.userName
        }
      }
    }
    </script>
    ```
    
- input값 URL에 인자 전달하기
1. router 만들기
    
    ```jsx
    <router-link :to="{ name: 'hello', params: { userName: 'myezi'} }">Hello</router-link>
    ```
    
2. input에 바인딩, keyup.enter
    
    ```jsx
    <input
        type="text"
        v-model="inputData"
        @keyup.enter="getName"
    >
    ```
    
3. router로 입력받은 이름 보내기
    
    ```jsx
    getName(){
       this.$router.push({ name: 'hello', params: { userName: this.inputData}})
    }
    ```
    

## lazy-routing

```jsx
{
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // => lazy-loading 방식
      // => 첫 로딩에 렌더링 하지 않고 해당 라우터가 동작할 떄 컴포넌트를 렌더링
    component: () => import('../views/AboutView.vue')
  },
```