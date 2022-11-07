# Vue Cli 프로젝트 시작하기_Node.js

---

---

# **Vue Cli**

### 브라우저 밖에서도 구동할 수 있는 런타임 환경

- 자바스크립트는 브라우저를 조작하는 유일한 언어이지만 브라우저 밖에서는 구동할 수 없음
- 자바스크립트를 구동하기위한 런타임 환경인 Node.js로 브라우저가 아닌 환경에서도 구동할 수 있게되었음

### NPM(Node Package Manage)

- 자바스크립트 패키지 관리자 (파이썬에서 pip)
- 다양한 의존성 패키지를 관리
- Node.js의 기본 패키지 관리자
- Node. js 설치 시 함께 설치된다

### Vue CLI

- Vue 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
- 확장 플러그인, GUI, Babel 등 다양한 tool 제공

---

# **Vue CLI 환경설정**

- git bash에서

```bash
npm install -g @vue/cli
```

- VScode terminal에서 프로젝트 생성

```bash
vue create vue-cli
```

```bash
Vue CLI v5.0.8
? Please pick a preset: (Use arrow keys)
> Default ([Vue 3] babel, eslint) 
  Default ([Vue 2] babel, eslint) 
  Manually select features
```

- 프로젝트 폴더로 이동해야함

```bash
cd vue-cli/`
```

- 서버 켜보기

```bash
npm run serve
```

![Untitled](Vue%20Cli%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5_Node%20js%200ef982daa096483c85aa443cb746c053/Untitled.png)

---

## 프로젝트 구조

![Untitled](Vue%20Cli%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5_Node%20js%200ef982daa096483c85aa443cb746c053/Untitled%201.png)

- *주의사항) .git이 들어있는데 상위폴더가 .git이 포함된 폴더라면 vue-cli 폴더는 제대로 올라가지 않음. vue-cli 폴더 안에 있는 .git을 지워줘야함!*
- node_modules
    - node.js 환경의 의존성 모듈
    - 파이썬에서 venv와 유사하기때문에 .gitignore에 추가해야함
- Babel
    - **JS의 complier**
    - JS의 ES6+코드를 구 버전으로 번역해주는 도구
    - 브라우저 버전별로 최신문법이 작동하지 않는 문제를 해결하기위한 도구
- Webpack (node_modules)
    - **static module bundler**
    - 모듈 간 의존성 문제를 해결하기 위한 도구
    - 프로젝트에 필요한 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함
- package.json : 프로젝트의 종속성 목록
- package-lock.json
    - requirements.txt의 역할
    - node-modules에 설치되는 모든 의존성 설정 및 관리
    - 개발과정간의 의존성 패키지 충돌 방지
- src
    - src/assets : 정적 파일을 저장하는 디렉토리
    - src/components : 하위 컴포넌트들이 위치
    - src/**App.vue** : **최상위 컴포넌트. public/index.html과 연결된다**
    - src/main.js : index와 App.vue를 연결시키는 작업이 이뤄지는 곳

## module

- 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워진다
- 따라서 자연스럽게 파일을 여러개로 분리하여 관리
    - 이때 분리된 파일 각각이 모듈 (js 파일 하나가 모듈)
- 모듈은 기능단위로 분리~ 클래스 하나 혹은 특정한 목적을 가진 여러개의 함수로 구성된 라이브러리
- 여러 모듈 시스템이 있음(ESM, AMD, CommonJS, UMD)

### Modul 의존성 문제

- 모듈이 많아지고 모듈 간 의존성이 깊어지고 복잡해지면서 문제 발생시 어떤 것의 문제인지 파악이 어려움
- Webpack은 모듈간 의존성 문제를 해결하기 위해 등장

## Bundler

- 모듈 의존성 문제를 해결해주는 작업이 Bundling
- Webpack is one of Bundler
- 모듈을 하나로 묶어주고 묶인 파일은 여러개 혹은 하나로 만들어줌
- Bundling된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작하게 된다
- webpack이외에 snowpack, parcel, rollup.js 등 다양한 모듈 번들러가 존재

![node_modules의 의존성 깊이..블랙홀보다 깊다](Vue%20Cli%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5_Node%20js%200ef982daa096483c85aa443cb746c053/Untitled%202.png)

node_modules의 의존성 깊이..블랙홀보다 깊다

### [deno 디노](https://deno.com/deploy)

- node.js를 만든 라이언 달이 만든 런타임
- node.js를 만들면서 후회하는 10가지.. 그래서 디노를 만듦

![Untitled](Vue%20Cli%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5_Node%20js%200ef982daa096483c85aa443cb746c053/Untitled%203.png)

![Untitled](Vue%20Cli%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5_Node%20js%200ef982daa096483c85aa443cb746c053/Untitled%204.png)

![Untitled](Vue%20Cli%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5_Node%20js%200ef982daa096483c85aa443cb746c053/Untitled%205.png)

![Untitled](Vue%20Cli%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5_Node%20js%200ef982daa096483c85aa443cb746c053/Untitled%206.png)

---

# SFC

## Component

- UI를 독립적이고 재사용 가능한 조각들로 나눈 것.**기능별로 분화한 카드조각**
- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성요소를 의미
- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임
    - body tag를 root node로 하는 tree구조
    - **vue에서도 App.vue를 root node로 하는 tree구조**
- 컴포넌트는 **유지보수**를 쉽게 만들어주고 **재사용성**의 측면에서도 매우 강력한 기능을 제공

### Component based architecture 의 특징

- 관리가 용이
    - 유지/보수 비용 감소
- 재사용성
- 확장가능
- 캡슐화
- 독립적

### Vue에서 Component는 new Vue()

- Vue CLI가 Vue를 Component based하게 도와준다

### SFC (Single File Component)

- 하나의 .vue 파일이 하나의 Vue instance이고 하나의 컴포넌트
- Vue instance에서는 HTML, CSS, JavaScript코드를 한번에 관리. 이 Vue instance를 **기능 단위로 작성하는 것이 핵심**
- 컴포넌트 기반 개발의 핵심 기능

![HelloWorld.vue 가 template안에서 하나의 component로 사용되는 것 확인 ](Vue%20Cli%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5_Node%20js%200ef982daa096483c85aa443cb746c053/Untitled%207.png)

HelloWorld.vue 가 template안에서 하나의 component로 사용되는 것 확인 

## Vue Component 구조

- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만든다
- 결국 index.html **하나의 파일만을 렌더링하는 과정 ⇒ SPA**

> 템블릿
> 
- HTML body부분

> 스크립트(Java Script)
> 
- 컴포넌트 정보, 데이터 ,메서드 등 vue 인스턴스를 구성하는 대부분이 작성된다
- const app = new Vue() 를통해 인스턴스를 생성하는 작업이 사라졌다
- 파일 자체가 컴포넌트이기 때문

```bash
export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
```

> 스타일 (CSS)
> 

---

### 시작환경

- Vue CLI를 실행하면 이미 HelloWorld.vue라는 컴포넌트가 생성되어있고 App.vue에 등록되어 사용되고있음
- npm run server 명령어 실행시 나오는 화면이 HelloWorld.vue

### MyComponent.vue

![Untitled](Vue%20Cli%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5_Node%20js%200ef982daa096483c85aa443cb746c053/Untitled%208.png)

1. src/componets/안에 생성
    - vue + enter 로 기본 틀 생성
2. script에 이름등록
    - script 안에 name 추가해서 상위컴포넌트에서 인식하도록
    - 파일명과 달라도 상관 없음! 사용할 때 동일하게 사용하면 되는것
3. templates에 요소 추가
    - 반드시 컴포넌트를 구성하는 최상위 태그가 있어야 에러가 나지 않음..!

### Component 등록 3단계

1. 불러오기
    
    ```bash
    import MyComponent from './components/MyComponent.vue'
    ===
    import MyComponent from '@/components/MyComponent'
    ```
    
    - @는 src폴더의 절대경로.
    - .vue 생략가능
    - import name은 해당 파일에서 설정한  name
2. 등록하기
    
    ```jsx
    components: {
        HelloWorld,
        // 2. 등록하기
        MyComponent,
      }
    ```
    
3. 보여주기
    
    ```jsx
    <template>
      <div id="app">
        <img alt="Vue logo" src="./assets/logo.png">
         <!-- 3. 보여주기 -->
        <MyComponent/>
        <HelloWorld msg="Welcome to Your Vue.js App"/>
      </div>
    </template>
    ```
    

### 하위컴포넌트

- MyComponent와 똑같은 과정으로 만들고 MyComponent 내부에 import-등록-보여주기 하면 하위 컴포넌트로 사용할 수 있음
- div안에 여러개 작성하면 같은 컴포넌트를 여러개 쉽게 불러올 수 있음
- 배열을 하위컴포넌트 여러개로 불러오기
    - ⇒ 도전🥞

### Component Name Style Guide

- 싱글 파일 이름 : **Filenames of [single-file components](https://vue2.hphk.io/v2/guide/single-file-components.html) should either be always PascalCase or always kebab-case.**
    - Pascal이나 kebab 하나만 써라
- 베이스 파일 이름 : **Base components (a.k.a. presentational, dumb, or pure components) that apply app-specific styling and conventions should all begin with a specific prefix, such as `Base`, `App`, or `V`.**
    - Base 혹은 App, V 로 시작하게 해라
- 강한 연관성을 가진 컴포넌트 : **Child components that are tightly coupled with their parent should include the parent component name as a prefix.**
    - 자식 컴포넌트는 부모 컴포넌트 이름을 포함하도록 한다