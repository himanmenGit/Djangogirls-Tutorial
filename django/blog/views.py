from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post


def post_list(request):
    # 1. 브라우저에서 요청
    # 2. 요청이 runserver로 실행 중인 서버에 도착
    # 3. runserver는 요청을 Django code로 전달
    # 4. Django code중 config.urls모듈이 해당 요청을 받음
    # 5. config.urls모듈은 ''(admin/을 제외한 모든 요청)을 blog.urls모듈로 전달
    # 6. bolg.urls모듈은 받은 요청의 URL과 일치하는 패턴이 있는지 검사
    # 7. 있다면 일치하는 패턴과 연결된 함수(view)를 실행
    #   7-1. settings 모듈의 TEMPLATES속성 내의 DIRS목록 에서
    #        blog/post_list.html파일의 내용을 가져옴
    #   7-2. 가져온 내용을 적절히 처리(렌더링, render()함수)하여 리턴
    # 8. 함수의 실행 결과(리턴값)을 브라우저로 다시 전달

    # HTTP 프로토콜 텍스트 데이터 응답을 반환
    # return HttpResponse('<html><body>'
    #                     '<h1>Post list<h1>'
    #                     '<p>Post 목록을 보여줄 예정 입니다.</p>'
    #                     '</body></html>')

    posts = Post.objects.all().order_by('-created_date')
    # render() 함수에 전달할 dict객체 생성
    context = {
        'posts': posts,
    }
    # 'blog/post_list.html' 템플릿 파일을 이룔해 HTTP프로토콜에 대해 응답함.
    # return render(
    #     request=request,
    #     template_name='blog/post_list.html',
    #     context=context,
    # )
    # 위 return 코드와 같음
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    """
    localhost:8000/detail/로 온 요청을
    'blog/post_detail.html'을 render한 결과를 리턴

    ursl, views, template을 모두 작성 해야 함

    :param request: request요청
    :param pk: primary key
    :return: blog/post_detail.html
    """

    context = {
        'post': Post.objects.get(pk=pk),
    }

    return render(request, 'blog/post_detail.html', context)


def post_add(request):
    # localhost:8000/add로 접근 시
    # 해당 뷰가 실행되어서 Post add page라는 문구를 보여주도록 urls작성
    # HttpResponse가 아니라 blog/post_add.html을 출력
    # post_add.html은 base.html을 확장, title(h2)부분에 'Post add'라고 출

    context = {

    }
    if request.method == 'POST':
        # 요청의 method가 POST일 때
        # HttpResponse로 POST요청에 담겨온
        # title과 content를 합친 문자열 데이터를 보여줌
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(
            author=request.user,
            title=title,
            content=content,
        )
        # post-detail이라는 URL name을 가진 뷰로
        # 리디렉션 요청을 보냄
        # 이 때, post-detail URL name으로 특정 URL을 만드려면
        # pk값이 필요하므로 키워드 인수로 해당 값을 넘겨 준다.
        return redirect('post-detail', pk=post.pk)
        # return HttpResponse(f"{post.pk} {post.title} {post.content} ")
    else:
        # 요청의 method가 GET일 때
        return render(request, 'blog/post_add.html', context)


def post_delete(request, pk):

    # pk에 해당하는 Post를 삭제
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()

    # 삭제후 post-list로 리디렉트
    return redirect('post-list')