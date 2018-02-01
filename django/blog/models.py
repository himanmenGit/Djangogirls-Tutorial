from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    # ForeignKey 는 다른 테이블과 연결됨 auth 테이블의 User 컬럼과 연결됨
    author = models.ForeignKey(
        'auth.User',
        # django 2.0 추가 사항
        # 유저 삭제시 연결된 테이블들의 내용을 같이 삭제
        on_delete=models.CASCADE,
    )
    # CharField 는 글자수 제한 하여 저장
    title = models.CharField(max_length=200)
    # TextField 는 글자수 제한 없이 저장
    content = models.TextField(blank=True)
    # DateTIleField 는 날짜와 시간을 나타냄
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    class Meta:
        verbose_name = '글'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ['-created_date']

    def publish(self):
        self.published_date = timezone.now()
        # 객체를 변환 시키고 데이터베이스에 저장해야 한다.
        self.save()

    def __str__(self):
        return self.title
