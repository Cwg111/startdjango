from django.shortcuts import render, HttpResponse
from .forms import MessageBoardForm,RegisterForm
# 请求验证装饰器
from django.views.decorators.http import require_http_methods

# Create your views here.
# 请求的method
# 1.GET：用来从服务器上获取数据
# 2.POST：用来向服务器提交数据
@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "GET":
        form = MessageBoardForm()
        return render(request, "index_2.html", context={"form": form})
    else:
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            # 即使用户输入的数据是符合form中的字段验证规则，也要对用户输入的数据进行清理，也就是cleaned_data
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            email = form.cleaned_data.get("email")
            return HttpResponse(f"{title},{content},{email}")
        else:
            print(form.errors)
            return HttpResponse("表单验证失败!")

@require_http_methods(["GET", "POST"])
def register_view(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get("telephone")
            return HttpResponse(f"{telephone}")
        else:
            print(form.errors.as_json())
            return HttpResponse("表单验证失败!")



