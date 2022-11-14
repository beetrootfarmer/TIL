# Vue 게시판

- 목차
    
    

---

## 기본 설정

`vue create articles`

`cd articles`

`vue add vuex`

`vue add router`

# index

### 중앙저장소에 데이터 생성

```jsx
state: {
    article_id: 3,
    articles:[
      {
        id :1,
        title : '제목1',
        content: '내용1',
        createdAt: new Date().getTime(),
      },
      {
        id :2,
        title : '제목2',
        content: '내용2',
        createdAt: new Date().getTime(),
      }
    ]
  },
```

### router component 등록 | component: IndexView

```jsx
import IndexView from '../views/IndexView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
```

### index에서 computed로 state가져오기 | this.$store.state.articles

```jsx
<template>
  <div>
    <h1>Articles</h1>
    {{articles}}
  </div>
</template>

<script>
export default {
  name: 'IndexView',
  computed:{
    articles(){
      return this.$store.state.articles
    }
  }
}
</script>
```

### Article에서 데이터 전달, ArticleItems에서 데이터 props로 받기

```jsx
<template>
  <div>
    <h1>Articles</h1>
    {{articles}}
    <ArticleItem
      v-for='article in articles'
      :key="article.id"
      :article=article
      />
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem'
export default {
  name: 'IndexView',
  components:{
    ArticleItem,
  },
  computed:{
    articles(){
      return this.$store.state.articles
    }
  }
}
</script>

<style>

</style>
```

![Untitled](Vue%20%E1%84%80%E1%85%A6%E1%84%89%E1%85%B5%E1%84%91%E1%85%A1%E1%86%AB%209f82b0ddf4fb40c2a600965840debc57/Untitled.png)

---

# 글 생성

### 글 작성하고 데이터 state로

```jsx
<template>
  <div>
    <h1> 게시글 작성 </h1>
      <form @submit.prevent="createArticle" action="">
        <input type="text" v-model.trim="title"/>
        <br>
        <textarea type="text" v-model.trim="content"/>
        <input type="submit"/>
      </form>
      <router-link :to="{ name:'index' }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name: 'CreateView',
  data(){
    return {
      title:null,
      content: null,
    }
  },
  methods:{
    createArticle(){
      const title = this.title
      const content = this.content
      const payload = {
        title, content
      }
      this.$store.dispatch('createArticle', payload)
    }
  }
}
</script>

<style>

</style>
```

```jsx
mutations: {
    CREATE_ARTICLE(state, article){
      state.articles.push(article)
      state.article_id = state.article_id + 1
    }
  },
  actions: {
    createArticle(context, payload){
      const article = {
        id : context.state.article_id,
        title : payload.title,
        content: payload.content,
        createdAt : new Date().getTime()
      }
      context.commit('CREATE_ARTICLE', article)
    }
  },
```

### 글작성이 완료되면 다음 페이지로 넘겨주기

- CreateView > createArticle() 마지막에 추가

```jsx
this.$router.push({ name : 'index' })
```

---

## 상세페이지

### detail 라우터 등록

```jsx
import DetailView from '../views/DetailView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/:id',
    name: 'detail',
    component: DetailView
  },
```

### 상세 페이지에서 인자로 받은 article id로 데이터를 가져와 표출

- 페이지 생성될 떄 함수가 자동 실행되도록 created()에서 함수 호출
- optional chaining(?.) 앞의 평가 대상이 ubdefined나 null이면 
    에러가 발생하는 대신 undefined를 반환

```jsx
<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{article?.id}} </p>
    <p>글 제목 : {{article?.title}}</p>
    <p>글 내용 : {{article?.content}}</p>
    <p>작성 시간: {{article?.createdAt}}</p>
    <!-- optional chaining(?.) 앞의 평가 대상이 ubdefined나 null이면 
    에러가 발생하는 대신 undefined를 반환-->
		<router-link :to="{name : 'index'}">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  computed:{
    articles(){
      return this.$store.state.articles
    }
  },
  data(){
    return{
      article : null,
    }
  },
  methods:{
    getArticleById(id){
      // const id = this.$route.params.id
      for (const article of this.articles){
        // url로 받은 인자는 문자열이기때문에 형변환
        if (article.id === Number(id)){
          this.article = article
          break
        }
      }
    }
  },
  created(){
    // 페이지 생성될 떄 함수가 자동 실행되도록
    this.getArticleById(this.$route.params.id)
  }
}
</script>

<style>

</style>
```

- 유니코드로 되어있는 시간을 변환

```jsx
<p>작성시간 : {{ articleCreatedAt }}</p>
...
computed:{
    ...
    articleCreatedAt(){
      const article = this.article
      const createdAt = new Date(article?.createdAt).toLocaleString()
      return createdAt
    }
  },
```

### ArticleItem에서 detail 페이지로 연결 | this.$router.push({ name : 'detail', params:{id}})

```jsx
<template>
  <div @click="goDetail(article.id)">
    <p>글 번호 : {{ article.id }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props:{
    article:Object,
  },
  methods:{
    goDetail(id){
      this.$router.push({ name : 'detail', params:{id}})
    }
  }
}
</script>

<style>

</style>
```

---

## 삭제

```jsx
deleteArticle(){
      this.$store.commit('DELETE_ARTICLE', this.article.id)
      this.$router.push({name : 'index'})
    },
```

```jsx
DELETE_ARTICLE(state, id){
      state.articles = state.articles.filter((article)=> {
        return !(article.id === id)
      })
    }
```

## 404 not found

### id 주소보다 위에 써서 detail 페이지에 걸리지 않도록..임의적인 주소

```jsx
{
    path : '/404-not-found',
    name : 'NotFound404',
    component: NotFound404
  },
  {
    path: '/:id',
    name: 'detail',
    component: DetailView
  },
```

- 존재하지 않는 회원 번호 일 때

```jsx
getArticleById(id){
      // const id = this.$route.params.id
      for (const article of this.articles){
        // url로 받은 인자는 문자열이기때문에 형변환
        if (article.id === Number(id)){
          this.article = article
          break
        }
      }
      if (this.article === null){
        this.$router.push({name:'NotFound404'})
      }
    }
```

- 나머지… 존재하지 않는 주소일 때 404페이지로

```
{
    path: '*',
    redirect: {name : 'NotFound404'}
  }
```