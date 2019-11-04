from django import template

register = template.Library() # 기존 템플릿 라이브러리에

@register.filter
def hashtag_link(word):
    # word는 article 객체가 들어갈건데,
    # article의 content들만 모두 가져와서 그 중 해시태그에만 링크를 붙인다.
    content = word.content + ' '
    hashtags = word.hashtags.all()

    for hashtag in hashtags:
        # 공백을 포함해서 변경했기 때문에 변경 후의 모양에도 공백을 포함시켜야 한다.
        content = content.replace(hashtag.content + ' ', f'<a href="/articles/{hashtag.pk}/hashtag">{hashtag.content}</a> ')

    return content
    # 작업 후에는 서버를 껐다 켜야 적용된다.
