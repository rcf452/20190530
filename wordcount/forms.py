#app 밑에 forms.py 생성
from django import forms
from .models import Blog #장고에서 제공해주는 form과 우리가 만든 Blog model을 가지고 온다

class BlogForms(forms.ModelForm): #forms 안에 있는 ModelForm을 상속받아줌

    class Meta: #data들을 위한 data
        model = Blog #model이 blog라는 걸 알려준다.
        fields=('title', 'body', 'create_date',)