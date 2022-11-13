# 시험준비
---
1. 아래의 설명을 읽고 T/F 여부를 작성하시오
  • SPA는 Single Pattern Application의 약자이다.
    - False : Single Page Application

  • SPA는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고,
  이후부터는 페이지 갱신에 필요한 데이터만 전달받는다.
    - True
      ~~False : 정적 리소스는 빈 페이지만 전달받고 이후의 모든 데이터를 요청시에 전달받는다~~

  • Vue.js에서 말하는 ‘반응형’은 데이터가 변경되면 이에 반응하여,
  연결된 DOM이 업데이트되는 것을 의미한다.
    - True

  • v-bind 디렉티브는 “@“, v-on 디렉티브는 “:” shortcut(약어)을 제공한다.
    - False : 반대

  • v-model 디렉티브는 input, textarea, select 같은 HTML 요소와 단방향 데이터
  바인딩을 이루기 때문에 v-model 속성값의 제어를 통해 값을 바꿀 수 있다.
    - False : 양방향 데이터 바인딩을 이룬다.

---
2. MVVM은 무엇의 약자이고, 해당 패턴에서 각 파트의 역할은 무엇인지 간단히 서술하시오.
  - Model : 실제 데이터
  - View : 사용자에게 보이는 부분
  - Vue Model : View를 위한 모델. View와 연결되어 Action을 주고받음. Model이 변경되면 View Model도 변경

---
3. (a) message (b) new Vue (c) '#app'

4. v-if와 v-for를 비교해서 설명해보시오
- v-show(Expensive initial load, cheap toggle)
    - **표현식 결과와 관계없이 렌더링 되므로 초기 렌더링 비용이 더 높음**
    - **display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle비용은 적음**
- v-if (Cheap initial load, Expensive toggle)
    - **표현식이 false면 렌더링되지 않기때문에 초기 렌더링 비용이 더 낮음**
    - **단, 표현식이 자주 변경되는 경우 잦은 재 렌더링으로 비용증가**

5. T or F
- v-on method를 통한 data 조작도 가능?
  -> T
- v-bind JS의 속성값에 HTML를 사용하기위한 라이브러리 
  -> F 반대! HTML 의 속성값에 JS를 사용하기위한 라이브러리
- V-model instance와 DOM의 양방향 바인딩!
  -> T
- v-for는 key 속성과 함께 작성하는 것을 권장한다.
  -> True
- v-bind는 HTML class 속성에서는 오직 하나의 data와 연결할 수 있다.
  -> False. 여러 data와 연결할 수 있음
- emit 은 부모 컨텐츠로의 data를 전달할 수 있으며 조상 컴포넌트로 데이터를 바로
  보낼 수는 없다.
  -> True
6. v-if 와 v-for를 같이 사용하지 않기
- v-if가 먼저 계산되고 해당 처리 시점에 반복 변수인 user가 존재하지 않기 때문에 에러 발생 (2 버전에서는 v-for가 더 높은 우선순위를 가진다)
- Vue가 디렉티브 처리할 때 **v-if가 v-for보다 높은 우선순위를 가진다**
- 동시에 사용해야한다면
    - 목록의 항목을 필터링 할 경우 activeUsers 로 대체

7. method와 computed의 개념과 그 차이에 대해서 간단히 서술하시오.

* computed는 계산 결과가 변하기 전까지 함수를 재호출 하는 것이 아닌 계산된 값(캐싱되어있는 값) 을 반환하고 method는 사용할 때마다 함수를 호출해 계산함. 재계산이 적은 것에 computed로 주로 사용한다

8. Vue는 단방향 데이터 흐름을 지향하는 프론트엔드 프레임워크다.
공식문서를 참고하여 그 이유를 서술하시오.
 -> 데이터 변화에 따른 성능의 변화없이 DOM 객체를 갱신할 수 있고, 데이터 흐름이 단방향이라 코드를 이해하기 쉽고 데이터 추적과 디버깅이 쉽다 

9. Vuex에서 State, Getters, Mutations, Actions의 역할을 각각 서술하시오.
  - State는 data의 역할
  - Getters는 computed의 역할
  - Mutations는 methods의 역할 중 data에 직접 접근하는 역할
    - state를 변경할 수 있는 유일한 방법
      - mutations에 정의될 메서드들은 항상 동기적 로직만을 가지고 있어야한다
  - Actions는 methods의 역할 중 
    - 데이터 전처리 로직을 정의하고 commit()으로 mutations를 호출하는 역할
    - mutations와 달리 값을 직접 변경하는 로직은 작성하지 않음
    - context 객체를 인자로 받아서 store 파일 내에 있는 모든 요소에 접근할 수 있고 메서드 호출도 가능하지만 state 변경은 mutations 호출을 통해 진행
    - context.'state, dispatch, getters, commit' 값은 {commit} 등의 형태로 축약해서 사용하는 편이다
    - actions에서는 비동기 요청들도 같이 처리를 할 것인데 state의 변경은 mutations를 통해서만 변경할 것이므로 data의 예기치 못한 변경 혹은 비동기처리가 모두 완료되고 난 후 정제된 data를 mutations에게 넘기는 역할을 한다

10. Vue Router에서 설정하는 history mode가 무엇을 뜻하는지 서술하시오.
  - Vue Router의 기본모드인 hash mode 가 URL이 변경될 때까지 페이지를 다시 로드하지 않는데 이러한 해시를 제거하기 위해 사용하는 모드. 페이지를 로드하지 않고도 URL 탐색을 할 수 있다. 

11. 동적으로 인자를 주소로 전달했을 때 해당 변수에 접근하는 방법은 $router.params
를 이용해서 접근할 수 있다.

12. 특정 라우트에 대해서만 가드를 설정하고싶을 때는 beforeEnter를 사용

13. lazy loading 를 사용하는 이유를 다음 공식 문서에서 확인하여 작성하시오.
  - 논 블럭상태로 자원을 사용하고 필요할 때만 로드하기위해서 사용하는 전략.  

14. 요청하는 경로가 없을 때 Not Found 404 페이지를 보여주는 코드
```javascript
    path : *,
    redirect : { name: 'NotFound404' }
```