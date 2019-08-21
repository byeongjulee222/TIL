from django.contrib import admin
from .models import Article # '.' : 명시적 상대경로 표현

# Register your models here.
class AriticleAdmin(admin.ModelAdmin):
    # 튜플이나 리스트로 작성 (대부분 튜플로 작성)
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    # 리스트에 필터 추가
    list_filter = ('created_at',) # 하나의 튜플 만들 때 뒤에 ',' 붙여줘야 함.
    # 항목에 링크 걸기
    list_display_links = ('content',)
    # 링크 안에 들어가지 않고 바로 수정할 수 있게
    list_editable = ('title',)
    # 한 페이지에 보이는 개수 조절 (기본값:100)
    list_per_page = 2

admin.site.register(Article, AriticleAdmin)
