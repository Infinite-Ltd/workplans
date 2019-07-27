from django.shortcuts import render
from core import models
from time import strftime
#from django_redis import cache
from django.views.decorators.cache import cache_page
from django.http import HttpResponse


# Create your views here.
def login(request):
    # username = request.POST.get('username')
    # password = request.POST.get('userpaw')
    # models.UserInfo.objects.create(userName=username, password=password)
    #models.UserInfo.objects.create(password=password)
    #print(username+' '+password)
    return render(request, 'loginPage.html')
def do_register(request):
    return render(request, 'register.html')

def register(request):
    print('$$$$$$$$$$')
    employeeId = request.POST.get('employeeId', None)
    aliasname = request.POST.get('aliasname', None)
    username = request.POST.get('username', None)
    password = request.POST.get('userpaw', None)
    isleader = request.POST.get('isleader', "false")
    dirleader = request.POST.get('dirleader', None)
    current_time = strftime('%Y-%m-%D,%H:%M:%S')
    if isleader=='true':
        isleader = True
    else:
        isleader = False
    try:
        models.Userinfo.objects.get(employeeId=employeeId)
        models.Userinfo.objects.get(userName=username)
    except Exception as e:
        models.Userinfo.objects.create(employeeId=employeeId, aliasName=aliasname, userName=username,
                                   password=password, isleader=isleader, dirLeader=dirleader,
                                   register_date=current_time)
        return render(request, 'homePage.html', {'user': aliasname})
    return  render(request, 'register.html')


#check userinfo

@cache_page(60*5, cache='redis', key_prefix='homepage')
def checkUser(request):
    username = str(request.POST.get('username'))
    password = request.POST.get('userpaw')
    #login_time =
    print(username, ' ', password)
    #models.Userinfo.objects.create(userName=username, password=password)

    # if request.method == 'post':
    #     pass
    #loginSuccess(request)
    try:
        user = models.Userinfo.objects.get(userName=username, password=password)
        aliasName = user.aliasName
        return render(request, 'homePage.html', {'user': aliasName})
    except Exception as e:
        return render(request, 'loginPage.html')


def loginSuccess(request):
    return render(request, 'homePage.html')


@cache_page(60*5, cache='redis', key_prefix='history')
def getHistory(request):
    #查询数据库
    history_data = [{"date": "2018-07-15", "content": '完成PUC语音功能的测试', "schedule": '90%', "comment": '工作有待改进',
                     'problem': '手台即兴爆炸'},
                    {"date": "2018-07-15", "content": '完成ICC系统搭建', "schedule": '100%', "comment": '值得表扬',
                     'problem': '研发时刻串门'},
                    {"date": "2018-07-15", "content": '完成与美女对接', "schedule": '90%', "comment": '工作有待改进',
                     'problem': '美女长得丑'}
                    ]
    return render(request, 'history_work.html', {"works": history_data})

def bad_request(request):
    return render(request, '400.html')

def page_not_fount(request):
    return render(request, '404.html')

def page_error(request):
    return render(request, '500.html')

def permission_denied(request):
    return  render(request, '403.html')

