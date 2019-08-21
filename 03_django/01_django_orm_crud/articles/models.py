from django.db import models

# Create your models here.
# 게시판 만들기 실습
class Article(models.Model):    # models.Model의 상속을 받는다.
    # id(프라이머리 키)는 기본적으로 처음 테이블 생성시 자동드로 만들어진다.
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10) # 클래스 변수(DB의 필드)
    content = models.TextField() # 클래스 변수(DB의 필드)
    created_at = models.DateTimeField(auto_now_add=True) # 클래스 변수(DB의 필드)
    updated_at = models.DateTimeField(auto_now=True) # 수정될 때마다 변경

    def __str__(self):
        return f'{self.pk}번 글 - {self.title} : {self.content}'