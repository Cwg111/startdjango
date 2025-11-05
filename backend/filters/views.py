from datetime import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"info": "欢迎您来到filters过滤器页面"}
    return render(request, "filters_index.html", context=context)


def filters_demo(request):
    values = [
        "1w",
        "hello world,hello Django!",
        {"birthday": datetime.now()},
        {"profile": "None"},
        None,
        {"html": "<h1>欢迎来到过滤器页面</h1>"},
    ]
    return render(request, "filters.html", context={"values": values})


def template_form(request):
    context = {"articles": ["小米su7", "ChatGPT 5发布"]}
    return render(request, "xfz_index.html", context=context)


def static_view(request):
    return render(request, "static.html")
