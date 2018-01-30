from django.urls import path

# 현재 패키지에서 views.py 모듈을 불러 온다.
# 상대 경로로 불러오는것을 권장함.
from . import views

# urlpatterns 예약된 속성 리스트
# 꼭 리스트의 형태로 작동 한다.
# 순서는?
urlpatterns = [
    # 일치하는 패턴에 대해 상응하는 모듈의
    # 함수자체를 전달
    path('', views.post_list),
    path('detail/', views.post_detail)
]
