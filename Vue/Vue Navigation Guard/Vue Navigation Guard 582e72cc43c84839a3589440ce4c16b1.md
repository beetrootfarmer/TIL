# Vue Navigation Guard

# lifecycle hook 이해하기

[Vue Router의 LifeCycle 이해하기](https://adeuran.tistory.com/14)

# Navigation Guard

- Vue router로 URL에 접근할 때 다른 url로 redirect하거나 해당 URL로의 접근을 막는 방법

종류

- 전역가드 : 애플리케이션 전역에서 동작
- 라우터 가드 : 특정 URL에서만 동작
- 컴포넌트 가드 : 라우터 컴포넌트 내에서 동작
- 라우터 객체가 생성되어있음

```
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
```

---

# Global Before Guard

- 다른 url로 이동할 때 항상실행
- router/index.js에 router.beforeEach()를 사용하여 설정
- 콜백함수의 값으로 3개의 인자를 받음
    - to : 이동할 URL정보가 담긴 Route 객체
    - from : 현재 URL정보가 담긴 Route 객체
    - next : 지정한 URL로 이동하기 위해 호출하는 함수
        - 콜백 함수 내부에서 반드시 한 번만 호출되어야함
        - 기본적으로 to에 해당하는 URL로 이동
- URL이 변경되어 화면이 전환되기 전 router.beforeEach()가 호출됨
    - 화면이 전환되지 않고 대기 상태가 됨
- **변경된 URL로 라우팅하기 위해서는 next()를 호출해줘야함**
    - next가 호출되기 전까지 화면이 전환되지 않음

```jsx
// router/index.js

router.beforeEach((to, from, next) => {
	console.log('to', to)
	console.log('from', from)
	console.log('next', next)
	next()
}
```

### 전역가드를 사용해서 Login 여부에 따른 라우팅 처리

> 로그인 되어있지 않다면 로그인 페이지로 이동하도록 next 설정
> 
1. 로그인 페이지 생성
2. 로그인 routes생성
3. 로그인뷰에 대한 router-link 추가
4. 로그인 여부에 따른 라우팅 처리
    
    ```jsx
    router.beforeEach((to, from , next) => {
      // 로그인 여부 임의 설정
      const isLoggedIn = false
    
      // 로그인이 필요한 페이지
      const authPages = ['hello']
    
      // 앞으로 이동할 페이지(to)가 로그인이 필요한 사이트인지 확인
      const isAuthRequired = authPages.includes(to.name)
    
      if (isAuthRequired && !isLoggedIn) {
        // (false일 경우)로그인 안되어있으면 login으로 이동하도록 
        console.log('Login으로 이동')
        next({ name : 'login'})
      }else {
        console.log('to로 이동')
        next()
      }
    })
    ```
    

---

# Router Guard

- 전체 라우트가 아닌 **특정 라우트에 대해서만 가드를 설정하고 싶을 때 사용**
- beforeEnter()
    - route에 진입했을 때 실행된다
    - 라우터를 등록한 위치에 추가
    - 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고
        
        다른 경로에서 탐색할 때만 실행된다
        
    - 콜백함수는 to, from ,next를 인자로 받는다

### 라우터 가드를 사용해 로그인 되어있다면 HomeView로 이동

```jsx
const isLoggedIn = true
...
const routes = [
{
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from , next){
      if (isLoggedIn === true){
        console.log('이미 로그인 되어있음')
        next({ name : 'home' })
      } else {
        next()
      }
    }
  }
]
```

---

# Component Guard

- 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
- input 데이터가 변경되었는데 hello 페이지에서 변경된 params가 적용되지 않음
    - hello **컴포넌트가 재사용되었기 때문에**
    - 기존 컴포넌트를 지우고 새로 만드는 것보다 효율적이지만
    - **lifecycle hook이 호출되지 않고 $router.params에 있는 데이터를 새로 가져오지 않는다**

### **beforeRoutepdate()**

- 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행
- params의 input데이터로 데이터를 재할당

```jsx
// HelloView.vue
beforeRouteUpdate(to, from ,next){
    this.userName = to.params.userName
    next() 
  }
```

---

## 404 Not Found

```jsx
{
    // 처리할 수 없는 주소가 오면 전부 다 404 페이지로 보내기 
    path: '*',
    redirect: '/404',
  }
```

### 형식이 유효하지만 특정 리소스를 찾을 수 없는 경우?

- 데이터가 없음을 명시
- 404 page로 이동

---

### 강아지 api로 품종 받아오는데 예외 만들기

- axios 설치 & import
    
    ```bash
    npm i axios
    ```
    
    ```jsx
    import axios from 'axios'
    ```
    
- 입력한 품종이 존재하지 않을 때 catch에서 404페이지로 redirect
    
    ```
    getDogImage(){
          const breed = this.$route.params.breed
          const dogImageUrl = `https://dog.ceo/api/breed/${breed}/images/random`
          axios({
            method : 'get',
            url: dogImageUrl,
          })
          .then((response) => {
            console.log(response)
            const imgSrc = response.data.message
            this.imgSrc = imgSrc
          })
          .catch((error) =>{
            // dog페이지에서 메세지 출력하는 대신
            // this.message = `${this.$route.params.breed}는 없는 품종입니다`
            // 404로 redirect
            alert(`${this.$route.params.breed}는 없는 품종입니다`)
            this.$router.push('/404')
            console.log(error)
          })
        }
    ```