from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method =="POST":#submit을 누르면 data를 Post로 보냄
        signup_form = UserCreationForm(request.POST) #3.Post로 보내면 일단 담아라
        if signup_form.is_valid:
            signup_form.save()#4. 저장
            return redirect('home') #내용 유효하면 index 이름의 url요청
        else:
            return redirect('signup') #내용 유효x signup이름의 url요청=> 다시 get->밑줄의 1번으로!!!!!
    signup_form = UserCreationForm()#회원가입에 필요한 form을 장고에서 제공해준다., 1.처음에는 get이라서 폼을 띄워준다
    return render(request, 'registration/signup.html', {'signup_form':signup_form})

