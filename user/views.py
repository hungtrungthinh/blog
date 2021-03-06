from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from article.models import Article
from user.models import User
from role.models import Role

# Create your views here.


def home(request):
    return HttpResponse("Hello User")


@csrf_exempt
def insert(request):
    """用户注册"""
    print(request.method)
    if request.method != 'POST':
        response_data = {'status': '405', 'message': '失败：请求方式错误，请使用POST方式', 'result': 'Method Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    param = json.loads(request.body.decode('utf-8'))

    try:
        username = param['username']
        password = param['password']
        role = param['role']
        User.objects.create(username=username, password=password, role=role)
        response_data = {'status': '200', 'message': '成功', 'result': username}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    except ValueError:
        response_data = {'status': '406', 'message': '失败：参数设置错误，请检查参数类型。', 'result': 'Method Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    except :
        response_data = {'status': '406', 'message': '失败：请检查是否参数不足。', 'result': 'some except is discovery'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def delete_by_id(request):
    id = request.GET.get('id')
    user_id = request.GET.get('user_id')
    print(id)
    print(user_id)
    result = User.objects.get(id=id)
    user_role = User.objects.get(id=user_id).role
    can_mange_user = Role.objects.get(id=user_role).can_mange_user

    if can_mange_user:
        response_data = {'status': '200', 'message': '成功。', 'result': '操作成功。'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
        result.delete()
    else:
        response_data = {'status': '407', 'message': '失败：用户权限不足。', 'result': 'Opened Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def select_by_id(request):
    id = request.GET.get('id')

    try:
        result = User.objects.get(id=id)
        print(result)
        return HttpResponse(result, content_type="application/json")

    except:
        response_data = {'status': '404', 'message': '失败：不存在。', 'result': 'Data Not Found'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def select_all(request):
    try:
        result = User.objects.all()
        result = serializers.serialize("json", result)
        return HttpResponse(result, content_type="application/json")
    except:
        response_data = {'status': '404', 'message': '失败：不存在。', 'result': 'Data Not Found'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def update_by_id(request):
    print(request.method)
    if request.method != 'POST':
        response_data = {'status': '405', 'message': '失败：请求方式错误，请使用POST方式', 'result': 'Method Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    param = json.loads(request.body.decode('utf-8'))

    try:
        id = param['id']
        title = param['title']
        content = param['content']
        user = param['user']

        result = Article.objects.get(id=id)
        user_role = User.objects.get(id=user).role
        can_mange_user = Role.objects.get(id=user_role).can_mange_user

        if can_mange_user:
            result.title = title
            result.content = content
            result.save()

            response_data = {'status': '200', 'message': '成功', 'result': title}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            response_data = {'status': '407', 'message': '失败：用户权限不足。', 'result': 'Opened Not Allowed'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")

    except ValueError:
        response_data = {'status': '406', 'message': '失败：参数设置错误，请检查参数类型。', 'result': 'Method Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

