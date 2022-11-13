

# README TEAM MINZI | yumin hyezi

> **09_PJT :: Vue를 활용한 SPA 구성**

​     

## 🎉 Goal

- 영화 정보를 제공하는 SPA 제작
- AJAX 통신과 JSON 구조에 대한 이해
- Vue CLI, Vue Router 플러그인 활용

   

🔵 모든 요구 사항 구현

🔵 제출기한 내에 제출

🔵 실습을 통한 이해

​     

## 🎬 사용 API

- TMDB API (필수)
- https://developers.themoviedb.org/3/movies/get-top-rated-movies

  ​     

## 💻 Problem

  ​     

### 1️⃣ 최고 평점 영화 출력

------
- 알고리즘
  1. TMDB API를 사용해 axios로 영화 데이터를 요청할 때 for문으로 10장의 페이지를 받아 영화리스트를 만들었습니다.
  2. `$store.dispatch()`로 영화 리스트를 store에 저장하는 action을 호출하고 mutation을 호출해서 영화를 저장했고 `getMovieList()`함수는 `created()`시 호출되도록 만들었습니다.
  3. MovieView에서 store의 영화 데이터를 받아오고 v-for로 영화 개별 데이터를 MovieCard 컴포넌트를 통해 표출했습니다.
- 어려웠던 점
  1. 영화 데이터를 여러 페이지 받아올 때 리스트 전개구문을 사용하는 부분이 어려웠습니다. 
  ```javascript
    this.movieList = [...this.movieList, ...response.data.results]
  ```
  2. API를 가져오는 과정에서 페이지 때문에 params를 사용하지 않았습니다. 
    - 그대신 API_URL에 바로 변수를 지정해주었음 
  ```javascript
   const API_URL = `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=en-US&page=${i}`
  ```
  3. 영화 개별 카드에 hover를 적용해서 제목과 상세설명을 띄워주는 부분이 어려웠습니다. 
  - 카드에 hover시 형제 컴포넌트인 텍스트 박스의 속성이 바뀌고 버튼을 클릭해야하는데 버튼에 마우스가 올라가면 카드에서 hover가 해제되기 때문에 깜빡거리는 이슈가 있었습니다. 
  - z-index를 사용하고, 이미지의 opacity를 변경하는 것 대신 텍스트 컴포넌트에 배경 색을 바꾸는 것으로 해결했습니다.



​     

### 2️⃣ 최고 평점 영화 중 랜덤 영화 한 개 출력

------
- 알고리즘
1. 랜덤 view를 렌더링할 때 `randomMovie()` 메소드를 호출합니다
2. 랜덤한 숫자를 생성해서 영화 목록의 pk값으로 사용해 영화 한 편의 데이터를 불러왔습니다

- 어려웠던 점
1. 랜덤 함수를 처음에 사용했다가 getters의 메소드가 두번 씩 호출되는 이슈가 있었습니다. 그래서 lodash의 `_.sample(_.range)`을 사용해서 일부 문제를 해결했으나 한 번씩 메소드가 두번 씩 호출되는 이슈가 남아있습니다.
  ```javascript
  const randomNumber = _.sample(_.range(0, 20))
  ```
​       

​       

### 3️⃣ 보고 싶은 영화 등록 및 삭제하기

------
- 알고리즘
1. input 태그에 영화제목을 입력받고 addMovie() 메소드로 입력받은 title과 selected를 담아 영화 Object를 생성했습니다
2. WatchListItem 컴포넌트에서 리스트로 출력했습니다.
3. MovieView의 movie list에서 원하는 영화 추가할 수 있도록 영화 카드 hover시 버튼을 추가했습니다.
- 어려웠던 점
1. 부트스트랩의 css와 원하는 요소가 충돌해서 마지막에 부트스트랩 컴포넌트를 제거하고 직접 vanila css를 추가했습니다.
2. 처음에 create가 안되었는데 watchMovieList를 watchMovie로 잘못 작성했던 이슈였습니다.

​      

## 🔥 Result
### MovieView
<img width="1320" alt="like" src="https://user-images.githubusercontent.com/87971876/201450829-c7749ac6-810e-4d48-a7f0-2a3b37d78d6f.png
">
### RandomView
### WatchListView

​     

## ✅ Review

- **[필수] 변수명 중요!!!**
- **[필수] 오타 유의!!!**

​        

- *API 이해하기*   

- **`Vuex` 전체  학습하기**
  - *css+bootstrap 공부하기* 
  - *javascript 공부하기* 