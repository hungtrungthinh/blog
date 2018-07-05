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
    return HttpResponse("Hello Role")


@csrf_exempt
def insert(request):
    print(request.method)
    if request.method != 'POST':
        response_data = {'status': '405', 'message': '失败：请求方式错误，请使用POST方式', 'result': 'Method Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    param = json.loads(request.body.decode('utf-8'))

    try:
        name = param['name']
        del_article = param['del_article']
        edit_article = param['edit_article']
        can_mange_role = param['can_mange_role']
        can_mange_user = param['can_mange_user']
        can_mange_article = param['can_mange_article']
        Role.objects.create(name=name, del_article=del_article, edit_article=edit_article,
                            can_mange_role=can_mange_role, can_mange_user=can_mange_user,
                            can_mange_article=can_mange_article)
        response_data = {'status': '200', 'message': '成功', 'result': name}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    except ValueError:
        response_data = {'status': '406', 'message': '失败：参数设置错误，请检查参数类型。', 'result': 'Method Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def delete_by_id(request):
    id = request.GET.get('id')
    user_id = request.GET.get('user_id')
    print(id)
    print(user_id)
    result = Role.objects.get(id=id)
    can_mange_role = result.can_mange_role

    if can_mange_role:
        response_data = {'status': '200', 'message': '成功。', 'result': '操作成功。'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
        result.delete()
    else:
        response_data = {'status': '407', 'message': '失败：用户权限不足。', 'result': 'Opened Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def select_by_id(request):
    try:
        id = request.GET.get('id')
        result = Role.objects.get(id=id)
        return HttpResponse(result, content_type="application/json")

    except:
        response_data = {'status': '404', 'message': '失败：不存在。', 'result': 'Data Not Found'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def select_all(request):
    try:
        result = Role.objects.all()
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
        name = param['name']
        del_article = param['del_article']
        edit_article = param['edit_article']
        can_mange_user = param['can_mange_user']
        can_mange_article = param['can_mange_article']

        result = Role.objects.get(id=id)
        can_mange_role = result.can_mange_role

        if can_mange_role:
            result.name = name
            result.del_article = del_article
            result.edit_article = edit_article
            result.can_mange_role = can_mange_role
            result.can_mange_user = can_mange_user
            result.can_mange_article = can_mange_article
            result.save()
            response_data = {'status': '200', 'message': '成功', 'result': name}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            response_data = {'status': '407', 'message': '失败：用户权限不足。', 'result': 'Opened Not Allowed'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    except ValueError:
        response_data = {'status': '406', 'message': '失败：参数设置错误，请检查参数类型。', 'result': 'Method Not Allowed'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

