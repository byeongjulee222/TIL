from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail
from django.urls import reverse
from django.db import models

# def articles_image_path(instance, filename):
#     return f'articles/{instance.pk}/images/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    # image_thumbnail = ImageSpecField(
    #     source='image', # 원본 ImageField 이름
    #     processors=[Thumbnail(200, 300)],
    #     format='JPEG',
    #     options={'quality': 90},
    # )
    image = ProcessedImageField(
        # ProcessedImageField에 인자로 들어가 있는 값들은 migrations 이후에
        # 추가되거나 수정되더라도 makemigrations를 하지 않아도 된다.
        processors=[Thumbnail(200, 300)], # 처리할 작업 목록
        format='JPEG', # 저장 포맷
        options={'quality': 90}, # 추가 옵션들
        upload_to='articles/images', # 저장 위치 (MEDIA_ROOT/article/images)
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        return reverse('articles:detail', kwargs={'article_pk': self.pk}) # /articles/10/
        '''
        딕셔너리로 작성할 때
        return reverse('articles:detail', kwargs={'pk':self.pk}) # /articles/10/
        '''
        # 주의사항
        # reverse 함수에 args랑 kwargs를 동시에 인자로 보낼 수 없다.


class Comment(models.Model):
    # comment_set 붙이는 것을 comments로 바꾸려면 --> , related_name='comments' 추가
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 가장 최신 댓글이 가장 위에 올라오도록
        ordering = ['-pk']

    def __str__(self):
        # return self.content
        return f'<Article({self.article_id}): Comment({self.pk})-{self.content}'


class Question(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Choice(models.Model):
    content = models.CharField(max_length=15)
    votes = models.IntegerField()

    def __str__(self):
        return self.content

