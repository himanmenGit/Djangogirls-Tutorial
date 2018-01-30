from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# urlpattern을통해 들어와서 처리해주는 곳


def post_list(request):
    # 1. 브라우저에서 요청
    # 2. 요청이 runserver로 실행 중인 서버에 도착
    # 3. runserver는 요청을 Django code로 전달
    # 4. Django code중 config.urls모듈이 해당 요청을 받음
    # 5. config.urls모듈은 ''(admin/을 제외한 모든 요청)을 blog.urls모듈로 전달
    # 6. bolg.urls모듈은 받은 요청의 URL과 일치하는 패턴이 있는지 검사
    # 7. 있다면 일치하는 패턴과 연결된 함수(view)를 실행
    # 8. 함수의 실행 결과(리턴값)을 브라우저로 다시 전달

    # HTTP 프로토콜 텍스트 데이터 응답을 반환
    return HttpResponse('<html><body>'
                        '<h1>Post list<h1>'
                        '<p>Post 목록을 보여줄 예정 입니다.</p>'
                        '</body></html>')
