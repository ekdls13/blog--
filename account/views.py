from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate #장고에서 제공해주는 login관련 메소드
# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid(): #폼이 정확한지 체크한후 폼의 데이터 가져옴
            username = form.cleaned_data.get("username") #form.is_valid를 통과한 데이터-username작성
            password = form.cleaned_data.get("password") #form.is_valid를 통과한 데이터-password작성
            user = authenticate(
                request=request, username=username, password=password) #authenticate명령어 사용시 login시 user정보가 넘어오게됨 

            if user is not None: #authenticate되지 않았을경우
                login(request, user)
                return redirect("list")
    else:
        form = LoginForm()
        return render(request, "account.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        # 우리가 폼으로 받은 데이터로 유저를 만들어야하기 때문에
        form = RegisterForm(request.POST)
        
        if form.is_valid(): #폼이 정확한지 체크한후 폼의 데이터 가져옴
            user = form.save() #유저가 만들어진것!
            #회원가입 하자마자 로그인 된 상태 원한다면
            login(request, user)
            return redirect("list")
        return render(request, "account.html", {"form": form})

    else:
        form = RegisterForm()
        return render(request, "account.html", {"form": form})

   