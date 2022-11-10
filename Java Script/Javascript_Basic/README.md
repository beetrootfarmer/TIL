# Java Script 기초 (1)

---

- 목차

---

# 변수와 식별자

### 식별자(identifier) 표기법

- 변수를 구분할 수 있는 변수명
- 반드시 문자, 달러($), 밑줄(_)로 시작
- 대소문자를 구분, 클래스명 이외에는 소문자로 시작
- 예약어 사용 불가능(if, for, function)

- 카멜 케이스(lower-camel-case)
- 파스칼 케이스(PascalCase, upper-camel-case) : 첫 단어를 대문자로
- 대문자 스네이크 케이스(SNAKE_CASE) : 값이 바뀌지 않을 상수

## 변수 선언 키워드

1. let
    - 블록 스코프 지역 변수를 선언
    - 재할당가능 & 재선언 불가능
2. const
    - 블록 스코프 읽기 전용 상수 선언
    - 재할당 불가능 & 재선언 불가능
3. var
    - 변수를 선언
    - 재할당 가능 & 재선언 가능
    - 호이스팅 문제를 발생시키기 때문에 const와 let을 주로 사용
        - 호이스팅 : 함수 선언 이전에 참조가 가능하며 undefined를 반환하는 현상
    

### 선언 할당 초기화

- 선언 : 변수를 생성
- 할당 : 선언된 변수에 값을 저장
- 초기화 : 선언과 할당을 동시에

---

# 데이터 타입

![스크린샷 2022-11-05 오전 11.41.26.png](Java%20Script%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20(1)%20a07e9d695bc74faebabcdd6a32ab9719/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-11-05_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%258C%25E1%2585%25A5%25E1%2586%25AB_11.41.26.png)

### 원시타입

### Number : 정수 또는 실수형 숫자

- isNaN() : Number형 확인함수. is Not a Number 축약

### String : 문자열. 덧셈가능

- Template Literal(Backtick)을 사용하면 줄 바꿈이 되며 문자열 사이에 변수도 삽입할 수 있음
    
    ``반갑습니다 ${name} !``
    
- Template Literal : 내장된 표현식을 허용하는 문자열 작성 방식

### Empty Value

- null : 변수의 값이 없음을 명시할때. object타입임 === 설계당시 해결하지 못한 버그
- undefined : 변수 선언 이후 할당하지 않으면 자동 할당

### Boolean

- true of false
    
    ![스크린샷 2022-11-05 오전 11.50.26.png](Java%20Script%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20(1)%20a07e9d695bc74faebabcdd6a32ab9719/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-11-05_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%258C%25E1%2585%25A5%25E1%2586%25AB_11.50.26.png)
    

---

# 연산자

### 할당 연산자

```python
let c = 3
c *= 10
```

### 비교연산자

```jsx
3 < 2 //false
'Z' < 'a' // true
'가' < '나' // true
```

### 동등 연산자 (==) (boolean 반환)

- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

```jsx
4 == '5' - 1 //true
6 == '5' + 1 //false '5' + 1은 51, 문자열 더하기는 문자열로 반환
```

### 일치 연산자 (===)

- 피연산자의 값과 타입이 모두 같을 경우 true

```jsx
1 === '1' // flase
1 === Number('1') // true
```

### 논리 연산자

```jsx
true && false //false
true && true // true
1 && 0 //0 
0 && 1 //0 
4 && 7 //7 둘다 true면 뒤에꺼
```

```jsx
false || true // true
false || false // false
1 || 0 //1
0 || 1 //1
4 || 7 //4 둘다 true면 앞에꺼
```

### 삼항 연산자

```jsx
const result = Math.PI > 4 ? 'YEP' : 'NOPE'
// NOPE
```

---

# 조건문

### if

```jsx
if (조건표현식) {
  (실행 코드)
}
```

### switch

- 조건의 표현식이 어느 결과값에 해당하는지 판별
- break가 없으면 defaul문을 만날때까지 다음 조건문을 실행! (**Fall-through현상**)
- 조건이 많으면 if 문 보다는 switch문을 사용하는 것이 유지보수, 가독성 향상에 좋음

```jsx
switch(operator){
  case '+' :{
		console.log(a + b)
		break
	}
  ...
}
```

---

# 반복문

- while
- for
    
    ```jsx
    for ([초기문]; [조건문]; [증감문];){ }
    ```
    
- **for…in**
    - object 순회 시 사용
    - **객체순회**
    - 배열 순회 가능하지만 인덱스 순으로 순회한다는 보장 없기때문에 권장하지 않음..!
    
    ```jsx
    const fruits = { a: 'apple', b :'banana' }
    for (const key in fruits) {
    	console.log(key) // a, b
    	console.log(fruits[key]) // apple, banana
    }
    ```
    
- **for…of**
    - **iterable 순회**
    - 반복 가능한 객체를 순회할 때 사용
    - Array, Set, String
    
    ```jsx
    const numbers = [1, 2, 3, 4, 5]
    for (const number of numbers) {
    	console.log(number) // 1, 2, 3, 4, 5
    }
    ```
    
- for in 은 **속성 이름**을 통해 반복
for of 는 **속성 값**을 통해 반복
    
    ```jsx
    const arr = [10, 20, 30]
    for (const i in arr) { console.log(i)}
    	// 0, 1, 2
    for (const i of arr) { console.log(i)}
    	// 10, 20, 30
    ```
    
    - 배열을 순회할때 value를 사용해야한다면,, for of를 써야 원하는 값을 얻을 수 있다
    - in으로 순회한 movie 의 type은 **string**이고 console창에서 **0, 1, 2**…로 뜬다
        
        ![스크린샷 2022-11-07 오전 1.42.15.png](Java%20Script%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20(1)%20a07e9d695bc74faebabcdd6a32ab9719/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%258C%25E1%2585%25A5%25E1%2586%25AB_1.42.15.png)
        
    
    ```jsx
    // for (movie in movieInfo.results){
    //     console.log(movie)
    //     console.log(typeof(movie))
    // }
    for ( movie of movieInfo.results ){
        if (movie.vote_average >= 8.0){
            console.log(movie.title)
        }
    }
    ```
    

---

# 함수 정의

JavaScript에서 함수를 정의하는 방법 

1. 함수 선언식 (functino declaraction)
2. 함수 표현식 (function expression)
- 공통점 : 데이터 타입, 구성요소
- 차이점 : 익명함수 가능여부, 호이스팅 발생여부

### 함수 선언식

```jsx
function 함수명(){ }
```

## 함수 표현식

```jsx
const result = function (n1, n2) { return ... }
```

```jsx
const result = function gogo(n1, n2) { return n1-n2 }
gogo(1, 2) // ReferenceError
result(1, 2) // 정상 작동. -1 리턴
```

```jsx
const result = function (name = 'Anonymous') { return ... }
```

```jsx
const result = function (n1, n2) { return  [n1, n2] }
result(1, 2, 3, 4) // [1, 2]
result(1) // [1, undefined]
```

---

# 전개구문 Spread Syntax

### 배열 복사

```jsx
let parts = ['shoulder', 'knees']
let lyrics = ['head', ...parts, 'and', 'toes']
// lyrics ['head', 'shoulder', 'knees', 'and', 'toes']
```

### 함수 restArgs

```jsx
const restOpr = function(arg1, arg2, ...restArgs){
	return [arg1, arg2, [restArgs]]
}
restOpr(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
```

---

# 선언식과 표현식함수의 호이스팅

### 선언식

- 함수 선언식 으로 정의한 함수는 var로 정의한 변수처럼 호이스팅이 발생

```jsx
add(2, 7) // 9
function add(a, b) { return a + b }
```

### 표현식

- 호이스팅이 없다. 함수 표현식으로 선언한 함수는 정의 전에 호출 시 에러 발생
- 표현식으로 정의한 함수는 **변수로 평가되기 때문에 scope 규칙을 따른다**

```jsx
add(2, 7) // Uncaugth ReferenceError
const add = function (a, b) { return a + b }
```

---

# Arrow Function

1. **function 키워드 생략 가능**
2. **함수의 매개변수가 하나면 ()도 생략 가능**
3. **함수의 내용이 한줄이면 {} 와 return 도 생략가능**

⚠️ 화살표 함수는 항상 익명함수이기 때문에 함수 표현식에서만 사용 가능

```jsx
const arrow1 = function(name) { return `hello, ${name}` }
// 1
const arrow1 = (name) => { return `hello, ${name}` }
// 2
const arrow1 = name => { return `hello, ${name}` }
// 3
const arrow1 = name => `hello, ${name}`
const arrow1 = name => (`hello, ${name}`) // return 안적으면 괄호 권장
```

### 화살표 함수 응용

1. 인자가 없다면? 
    
    ```python
    const fun = () => 'No args'
    ```
    
2. object를 return 한다면?
    
    ```python
    const returnOnj = () => { return { key: 'value'}}
    ```
    
3. return을 적지 않으려면? 괄호 필수
    
    ```python
    const returnObj = () => ( { key: 'value'} )
    ```
    

## 즉시 실행 함수(IIFE)

- 선언과 동시에 실행
- 함수 끝에 ()로 인자를 넘길 수 있음
- 일회성 함수이므로 익명함수로 사용하는 것이 일반적
    
    ```jsx
    (function(num) { return num *** 3 }) (2) //8
    (num => num ** 3) (2) //8
    ```
    

---

### Array and Object

- 참조타입에 해당하며 객체라고도 말한다

# Array

- 키와 속성을 담고있는 참조 타입의 객체
- **순서를 보장**함
- array.length로 배열의 길이 접근
- array.length-1로 마지막 인덱스 접근

## 배열 메서드

**reverse : 원본 배열의 순서를 반대로 정렬**

**push & pop : array.push() 배열의 가장 뒤에 추가 / array.pop() 배열의 마지막 요소 제거**

**unshift & shift : 배열 가장 앞의 요소를 추가,제거**

**includes : array.includes(V) V가 존재하는지에 대해 true of false 반환**

**indexOf : array.indexOf(V) V가 존재하면 인덱스 반환, 존재하지 않으면 -1 반환**

**join : array.join([seperator]) 배열의 모든 요소를 구분자로 연결하여 반환 (쉼표가 기본 구분자)**

> **호출 시 인자로 Callback 함수를 받는 메서드**
> 

**forEach**

- 인자로 주어지는 함수(콜백함수)를 배열의 각 요소에 대해 한 번씩 실행한다
- `array.forEach((element, index, array) => {})`
- **반환값 없음**
- break, continue 사용할 수 없음

**map**

- 배열의 각 요소에 대해 콜백함수를 한번씩 실행하고 **콜백함수의 반환값을 요소로 하는 새로운 배열 반환**
- forEach + return값
- `array.map((element, index, array) => {})`

```jsx
const numbers = [1, 2, 3]
    const doubleFunc = function(number) {
      return number * 2
    }
    const doubleNumbers = numbers.map(doubleFunc)
    console.log(doubleNumbers)
```

**filter**

- 배열의 각 요소에 대해 콜백 함수의 반환값이 true인 요소들만 모아서 새로운 배열을 반환
- 기존 배열요소들을 필터링 할 때 유용
- `array.filter((element, index, array) => {})`

```jsx
const menus = [
      {nema:'Vegan Lagu Pasta', type:'vege'},
      {nema:'shrimp cheese pizza', type:'pesco'},
      {nema:'Cashew Cheese Vege Pizze', type:'vege'},
      {nema:'Bulgogi Cream Risotto', type:'non-vegan'},
      {nema:'Gourmet Mushroom Risotto', type:'vege'},
    ]

    const vegefilter = function(product) {
      return product.type == "vege"
    }

		// 콜백으로 넘기는 부분
    const vege = menus.filter(vegefilter)

    console.log(vege)
```

```python
const vege = menus.filter( v => v.type == 'vege')
```

**find**

- 배열의 각 요소에 대해 콜백함수 반환값이 true인 첫번째 요소를 반환
- 찾는 값이 배열에 없으면 undefined 반환
- `array.find(callback(element[,index[,array]]))`

```jsx
const avengers = [
    {name: 'Tony Stark', age:45},
    {name: 'Steve', age : 32},
    {name: 'Thor', age:40},
  ]
  const avenger = avengers.find(function(avenger){
    return avenger.name == 'Tony Stark'
  })

  const avenger2 = avengers.find((avenger) => {
    return avenger.name == 'Tony Stark'
  })
```

**every**

- 배열의 모든 요소가 판별 함수를 통과하면 true, **하나라도 통과하지 못하면 false**
- 빈 배열은 항상 true
- `array.every((element, index, array) =>{})`

```jsx
const arr = [1, 2, 3, 4, 5]
  const result = arr.every((elem) =>{
    return elem % 2 === 0
// false
```

**some**

- 배열의 요소 중 **하나라도 주어진 판별 함수를 통과하면 참을 반환**
- **모든 요소가 통과하지 못하면 false**
- `array.some(callback(element[, index[, array]]))`

```jsx
const arr = [1, 2, 3, 4, 5]
  const result = arr.some((elem) =>{
    return elem % 2 === 0
// true
```

**reduce**

- 인자로 주어지는 함수(콜백함수)를 배열의 각 요소에 대해 한 번씩 실행해서 **누적된 하나의 결과 값을 반환**
- `array.reduce((acc, element, index, array) => {}, **initialValue**)`
- 배열을 하나의 값으로 계산하는 동작이 필요할 때 사용
- map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음
- acc는 이전 callback 함수의 반환값이 누적되는 변수

```jsx
const tests = [90, 95, 88, 77]

      const sum = tests.reduce(function (total, x){
        return total + x
      }, 0)

      const sum2 = tests.reduce((total, x) => total + x, 0)

      const sum3 = tests.reduce((total, x) => total + x, 0)/ tests.length
```

---

# Object

- 속성(property)의 집합이며 중괄호 내부에 key와 value 쌍으로 표현
1. key
    - **문자열 타입만 가능**
    - key이름에 띄어쓰기 등 구분자가 있으면 따옴표로 묶어서 표현
2. value
    - 모든 타입(함수포함) 가능
- 객체 접근
    - 점 혹은 대괄호
    - key이름에 띄어쓰기 같은 구분자가 있으면 대괄호만 사용 가능
    
    ```jsx
    const me = {
    	name: 'hyeji',
      number: '01012345678',
      'family':{
    		mom: 'Grace',
    		dad: 'Mark',
    	},
    }
    
    me.name === me['name']
    me['family'] != me.family // 불가능! 딕셔너리 .으로 접근 불가능
    me['family'].mom // 가능
    ```
    

## Object 문법

### 1. 속성명 축약

```jsx
let bookShop = {
  books, //books : books,
  megazines, //megazines : megazines,
}
```

### 2. 메서드명 축약

```jsx
const obj = {
	greeting() {        // greeting: function(){
		console.log('Hi') 
	} 
}
```

### 3. 계산된 속성명 사용하기

```jsx
const key = 'country'
const value = ['한', '미', '일', '중']

const myObj = {
	[key] : value,
}

console.log(myObj.country) // ['한', '미', '일', '중']
```

### 4. 구조분해 할당

```jsx
const me = {
	name: 'hyeji',
  number: '01012345678',
  'family':{
		mom: 'Grace',
		dad: 'Mark',
	},
}

const { name } = me // const name = me.name
const { mom, dad } = me['family'] 
```

### 5. Spread syntax (…)

- 얕은 복사에 활용가능

```jsx
const obj = {b:2, c:3, d:4}
const newObj = {a:1, ...obj, e:5}

console.log(newObj) // {a:1, b:2, c:3, d:4, e:5}
```

### JSON

- JSON은 Object 구조를 가진 ‘문자열’
- JSON을 Object로 사용하기 위해서는 변환작업이 필요함

```jsx
const jsonToObj = JSON.parse(objToJson)
```

```jsx
const objToJson = JSON.stringify(jsonObj)
```

---