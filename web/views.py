from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from utils.helper import check_code

class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入用户名", "name": "user"}),
        # 正则表达式
        # validators=[RegexValidator(r'^\w{6,}$',"用户名格式错误"),
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入密码", "name": "pwd"})
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入验证码"})

    )
def login(request):
    """ 注册 """
    form = LoginForm
    return render(request, "login.html", {"form": form})

def img_code(request):
    # 1.生成图片
    image_object, code_str = check_code()


    # 2.图片内容写入内存，从内存中读取并且返回
    stream = BytesIO()
    image_object.save(stream, 'png')

    return HttpResponse(stream.getvalue())



def home(request):
    """ 主页 """
    return HttpResponse("HOME")
