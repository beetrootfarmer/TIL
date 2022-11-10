from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        # 수정된 시간

    def __str__(self):
        return self.title

class Comment(models.Model):
    # 변수명 : 내가 참조하고 있는 대상의 이름을 소문자로 만들면 
    # table에서는 컬럼명_id로 컬럼 생성된다
    article = models.ForeignKey(Article, on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content