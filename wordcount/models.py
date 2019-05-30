from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model): #models 모듈에 있는 Model이라는 class
    title=models.CharField(max_length=200)
    # pub_date=models.DateTimeField('date published') #장고 내부 정의 속성
    body=models.TextField() #글자치는 공간-body
    create_date = models.DateField(default=timezone.now)

    def __str__(self): #self 말고 아무거나 써도 된다
        return self.title #설정안해주면 객체의 이름이 제목으로 뜬다.