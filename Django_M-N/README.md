# 다대다 구현

### N:1의 한계

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

**=> 예약테이블을 따로 만들어야하는 상황**

## 중개모델

예약모델은 의사와 환자에 각각  N:1 관계를 가짐 

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

- db 초기화
    1) migration 파일 (001...) 지우기
    2) .sqlite3 파일 지우기
- 다시 makemirations

### 의사1 환자1 예약생성

```bash
>>> doctor1 = Doctor.objects.create(name='alice')
>>> patient1 = Patient.objects.create(name='carol')
>>> doctor1
<Doctor: 1번 의사 alice>
>>> patient1
<Patient: 1번 환자 carol>
>>> Reservation.objects.create(doctor = doctor1, patient = patient1)
<Reservation: 1번 의사의 1번 환자>
```

### 의사 한명에 여러개의 예약이 있을 때 문제가 해결되는 부분 확인

```bash
>>> patient1.reservation_set.all()
<QuerySet [<Reservation: 1번 의사의 1번 환자>]>
>>> patient2 = Patient.objects.create(name='dane')
>>> patient2
<Patient: 2번 환자 dane>
>>> Reservation.objects.create(doctor = doctor1, patient = patient2)
<Reservation: 1번 의사의 2번 환자>
>>> doctor1.reservation_set.all()
<QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 1번 의사의 2번 환자>]>
```

---

## 다대다필드 만들기

```python
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor)
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

- 환자 모델에 의사를 추가하는데 
다대다모델에서는 복수형 doctors로 정의한다
- ManyToManyField() 사용
- 데이터베이스 초기화하고 다시 migration

**reservation 클래스 없이 환자와 의사 사이에 중계테이블이 생성된 것을 db에서 확인할 수 있음**

테이블 명 hospitals_patient_doctors
pk id:integer
-doctor_id:bigint
-patient_id:bigint

**이제 의사나 환자가 예약을 만들 수 있음**

```bash
In [2]: doctor1 = Doctor.objects.create(name='의사')
In [4]: patient1 = Patient.objects.create(name='환자')
In [5]: patient1.doctors.add(doctor1) # add()를 사용해서 참고
In [8]: patient1.doctors.all()
Out[8]: <QuerySet [<Doctor: 1번 의사 의사>]>

In [9]: doctor1.patient_set.all()
Out[9]: <QuerySet [<Patient: 1번 환자 환자>]> #의사 입장에서는 역참조임
```

**의사가 환자를 예약할 때**

```bash
In [12]: patient2 = Patient.objects.create(name='위급')

In [13]: doctor1.patient_set.add(patient2)

In [16]: doctor1.patient_set.all()
Out[16]: <QuerySet [<Patient: 1번 환자 환자>, <Patient: 2번 환자 위급>]>
In [17]: patient2.doctors.all()
Out[17]: <QuerySet [<Doctor: 1번 의사 의사>]>
```

### add와 마찬가지로 remove()를 양쪽에서 할 수 있다

```bash
In [18]: doctor1.patient_set.remove(patient1)
In [19]: patient2.doctors.remove(doctor1)
In [21]: doctor1.patient_set.all()
Out[21]: <QuerySet []>
```

---

## related_name 속성을 활용

-> 역참조시 set_으로 호출하지 않고 지정된 이름으로하도록 

```bash
doctors = models.ManyToManyField(Doctor, related_name='patients')
```

makemigrations 작업 다시

```bash
In [4]: doctor1.patients.all()
Out[4]: <QuerySet []>
# : doctor1.patient_set.all() 이제 사용할 수 없음 
```

---

### through 옵션

> → extra data가 있을 때(외래키 두 개로 부족할 때)는 중개테이블과ManyToMany 같이 사용해야함
> 

> → through 옵션을 사용하여 중계테이블에 테이터를 추가
> 

```python
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation') # 여기!
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

1. Reservation 클래스를 통한 예약생성

```bash
reser1 = Reservation(doctor=doctor1, patient = patient1, symptom='headache')
```

1. 환자 클래스를 통한 예약생성

```bash
patient2.doctors.add(doctor1, through_defaults={'symptom':'flu'})
```

---

# ManyToManyField

### 사용법

- `ManyToManyField(to, **options)`
- 다대다
- add(), remove(), delete()...

### 표현

- 테이블의 이름은 필드와 모델의 테이블 이름을 조합하여 생성된다

### arguments

- related_name
    - target model이 source model을 참조할 때 사용할 manager name
    - ForeignKey의 related_name과 동일
- through
    - 중개테이블을 직접작성할 경우 through옵션을 사용해 장고 모델을 지정
    - 중개테이블에 추가 데이터를 사용하는 경우
- symmetrical : 대칭
    - 기본값: True
    - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용 
    - 팔로우 테이블에서 사용된다
        symmetrical=False (대칭을 사용하지 않는 경우)
    -User - User 관계

## Related Manager

- N:1 혹은 M:N에서 사용 가능한 문맥
- 역참조 시에 사용

objects라는 매니저를 사용한 것 처럼 쿼리셋 api사용

- M:N관계에서는 관련된 두 객체에서 모두 사용
- add(), remove()

### methods

- add()
    - 환자 객체에 의사를 추가 (지정된 객체를 관련 집합에 추가한다)
    - 이미 존재하는 관계에 사용하면 관계가 복제되지 않는다
    - 모델 인스턴스, 필드값(PK)을 인자로 허용
- remove()
    - 관련 객체 집합에서 지정된 모델 개체를 제거
    - 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제된다
    - 모델 인스턴스, 필드 값(PK)를 인자로 허용

### 중계테이블 필드 생성 규칙

1. 소스 및 대상 모델이 다른 경우
- id
- 소스모델 아이디(patient_id)
- 대상 아이디(doctor_id)
2. ManyToMany가 동일한 모델을 가리키는 경우
- id
- from_<model>_id
- to_<model>_id

---

# M:N (Article-User)

좋아요기능 like

```python
# articles > models.py > Article class >
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
```

### 기존에 .article_set매니저가 사용되고있었기 때문에 related_name을 사용해야함

N:1보다는 M:N의 경우에 사용

```python
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```

### 모델관계 설정

```
- article.user : 게시글을 작성한 유저- N:1
- user.article_set : 유저가 작성한 게시글(역참조) - N:1
- articles.like_users : 게시글을 좋아요한 유저 - M:N
- user.like_articles : 유저가 좋아요한 게시글(역참조) - M:N
```