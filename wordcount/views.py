from django.shortcuts import render, redirect #render데이터 넘겨주기, redirect 해당페이지를 띄어줌 그러나 데이터 x
from .models import Blog
from .forms import BlogForms
from django.contrib.auth.decorators import login_required

# Create your views here.
# def index(request): #받아주고
#     return render(request, 'index.html') #index로 context 넘겨준다

# def result(request): #보내주고 한꺼번에 하면 받아주지 않았는데 넘겨준다고 오류??
#     a=request.GET['mytext'] #html에서 설정해준 form 이름
#     d = a.split(' ')
#     mydict={}
#     for i in d: #안에서 단어 i일 때
#         if i in mydict:#mydict 안에 단어가 있으면???
#             mydict[i]+=1 #단어횟수를 한번 추가해줘라
#         else :
#             mydict[i]=1 #없으면 단어와 횟수 한번을 해줘라
#     context={'b':a, 'mydict':mydict, 'myitem':mydict.items} #페이지간에 이동이 가능한 딕셔너리 context
#     return render(request, 'result.html', context)

def home(request):
    # blogs = Blog.objects #blogs-변수 Blog-class.object-queryset객체
    # return render(request, 'home.html', {'blogs':blogs})#모든 객체를 담은 blogs가 사전형으로 보내짐????
    blog_all = Blog.objects.all
    context={'blog_all' :blog_all}
    return render(request, 'home.html')

@login_required #로그인이 안된 상태면 자동으로 로그인 페이지로!!
def new(request):
    if request.method == 'POST':
        forms =BlogForms(request.POST)

        if forms.is_valid: #forms 안에 유효하면 forms을 모델에 저장
            forms.save()
            return redirect('new') #render는 html을 요청 redirect는 url 요청 한번더 처리 다음 페이지로 넘겨준다
    forms = BlogForms()
    return render(request,'new.html', {'forms': forms})


