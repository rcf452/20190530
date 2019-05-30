"""mywordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from wordcount import views
import wordcount.views
from accounts import views as ac_views #애칭지어주기
from django.contrib.auth.views import LoginView, LogoutView #class임
from portfolio import views as pviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home, name='home'),
    path('new/', wordcount.views.new, name="new"), #new라는 애칭을 지어준다. view에 있는 new라는 함수가 들어갈거임
    path('signup/', ac_views.signup, name="signup"),#회원가입 계정관련부분 /기능별로 구분=>app 새로 생성해야함
    path('login/', LoginView.as_view(), name="login"), #class로 만들어진 view
    path('logout/', LogoutView.as_view(), name="logout"), #class로 만들어진 view
    #CBV Class Based View, FBV Funtion Based View
    path('portfolio/', pviews.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
