import re
from django.urls import path, re_path

# 현재 패키지에서 views.py 모듈을 불러 온다.
# 상대 경로로 불러오는것을 권장함.
from . import views

# urlpatterns 예약된 속성 리스트
# 꼭 리스트의 형태로 작동 한다.
# 순서는?
urlpatterns = [
    # 일치하는 패턴에 대해 상응하는 모듈의
    # 함수자체를 전달
    path('list', views.post_list, name='post-list'),
    # path('detail/', views.post_detail)

    # 3/
    # 53/
    # 53/asdf/ <- X
    # pk가 view.post.detail 함수에 아규먼트로 자동으로 넘어감.
    # re_path(r'(?P<pk>\d+)/$', views.post_detail)
    path('post/<int:pk>/', views.post_detail, name='post-detail')

    # 숫자가 한개 이상 반복되는 경우를 정규표현식으로 구현 하되
    # 해당 반복 구간을 그룹으로 묶고, 그룹 이름을 'pk'로 지정
    # re.compile(r'(?P<pk>\d+)')
]
