from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
# Article 보다 먼저 정의해줘야 아래에서 참조할 수 있다(위쪽에 작성)
class Hashtag(models.Model):
    # 같은 해시태그가 작성되면 안됨.(unique)
    # unique=True인 경우 이 필드는 테이블 전체에서 고유한 값이어야 한다.
    # 유효성 검사 단계에서 실행되며 중복값이 있는 모델을 저장하려고 하면 .save() 메서드로 인해
    # 'IntegrityError'가 발생한다.
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content
    

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    # 해시태그 불러오기 전에 위에서 먼저 저의
    hashtags = models.ManyToManyField(Hashtag, blank=True, )


    class Meta:
        ordering = ('-pk',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"article_pk": self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.content
