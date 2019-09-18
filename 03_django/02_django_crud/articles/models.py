from django.urls import reverse
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        return reverse('articles:detail', args=[self.pk]) # /articles/10/
        '''
        딕셔너리로 작성할 때
        return reverse('articles:detail', kwargs={'pk':self.pk}) # /articles/10/
        '''
        # 주의사항
        # reverse 함수에 args랑 kwargs를 동시에 인자로 보낼 수 없다.
