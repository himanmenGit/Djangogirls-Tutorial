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
    path('', views.post_list, name='post-list'),
    # path('detail/', views.post_detail)

    # 3/
    # pk가 view.post.detail 함수에 아규먼트로 자동으로 넘어감.
    # re_path(r'(?P<pk>\d+)/$', views.post_detail)
    path('<int:pk>/', views.post_detail, name='post-detail'),

    # /3/delete/
    path('<int:pk>/delete/', views.post_delete, name='post-delete'),

    # /3/edit/
    path('<int:pk>/edit/', views.post_edit, name='post-edit'),

    # localhost:8000/add에 접근할 수 있는 path 구현
    # /add/
    path('add/', views.post_add, name='post-add'),

    # 숫자가 한개 이상 반복되는 경우를 정규표현식으로 구현 하되
    # 해당 반복 구간을 그룹으로 묶고, 그룹 이름을 'pk'로 지정
    # re.compile(r'(?P<pk>\d+)')
]
