from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from article.models import Article

# Create your views here.


def home(request):
    return HttpResponse("Hello Article")


@csrf_exempt
def insert(request):
    print(request.method)
    if request.method != 'POST':
        response_data = {'status': '405', 'message': '失败：请求方式错误，请使用POST方式', 'result': 'Method Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    param = json.loads(request.body.decode('utf-8'))

    try:
        title = param['title']
        content = param['content']
        user = param['user']
        Article.objects.create(title=title, content=content, user=user)
        response_data = {'status': '200', 'message': '成功', 'result': title}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    except ValueError:
        response_data = {'status': '406', 'message': '失败：参数设置错误，请检查参数类型。', 'result': 'Method Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def delete_by_id(request):
    id = request.GET.get('id')
    user_id = request.GET.get('user_id')
    print(id)
    print(user_id)
    result = Article.objects.get(id=id)
    if result.user == int(user_id):
        response_data = {'status': '200', 'message': '成功。', 'result': '操作成功。'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
        result.delete()
    else:
        response_data = {'status': '407', 'message': '失败：用户权限不足。', 'result': 'Opened Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def select_by_id(request):
    id = request.GET.get('id')
    result = Article.objects.get(id=id)
    return HttpResponse(result, content_type="application/json")



def select_all(request):
    result = Article.objects.all()
    result = serializers.serialize("json", result)

    return HttpResponse(result, content_type="application/json")


def update_by_id(request, id):
    if request.POST:
        res = Article.objects.get(id=str(id))
        print(res)
        return HttpResponse("Hello Article")
