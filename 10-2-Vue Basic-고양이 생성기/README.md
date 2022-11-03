# Vue Basic : 고양이 생성기

# 1. vue cdn, axios cdn

```jsx
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
```

```jsx
<script src="https://cdn.jsdelivr.net/npm/axios@1.1.2/dist/axios.min.js"></script>
```

[GitHub - axios/axios: Promise based HTTP client for the browser and node.js](https://github.com/axios/axios#cdn)

## 2. html 기본 틀 잡기

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>고양이</title>
</head>
<body>
  <div id="app">
    <h1>Cat Image</h1>
    <img :src="catUrl" alt="cat" style="height: 500px;">
    <button @click="showCat">고양이보여줘</button>
  </div>
</body>
</html>
```

### 3. img 태그에 data bind

```jsx
const app = new Vue({
      el:'#app',
      data:{
        catUrl:'',
      },
```

## 4. button 태그 클릭시 고양이 사진 띄우는 메서드

- axios 사용해서 응답(API_URL) 받을 시 then() 실행
- imgURL 객체에 응답 url 담아서
- image 태그 src에 담아주기

```jsx
methods:{
        showCat: function(){
          const API_URL = 'https://api.thecatapi.com/v1/images/search'
          axios.get(API_URL)
          .then((response) => {
            const imgURl = response.data[0].url
            this.catUrl = imgURl
          })
        }
      },
```

## 5. 완성

![Untitled](Vue%20Basic%20%E1%84%80%E1%85%A9%E1%84%8B%E1%85%A3%E1%86%BC%E1%84%8B%E1%85%B5%20%E1%84%89%E1%85%A2%E1%86%BC%E1%84%89%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B5%2009a4ce89bff74892b2069cbcaa62b4ba/Untitled.png)

![catUrl 바뀌는 것 확인](Vue%20Basic%20%E1%84%80%E1%85%A9%E1%84%8B%E1%85%A3%E1%86%BC%E1%84%8B%E1%85%B5%20%E1%84%89%E1%85%A2%E1%86%BC%E1%84%89%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B5%2009a4ce89bff74892b2069cbcaa62b4ba/Untitled%201.png)

catUrl 바뀌는 것 확인