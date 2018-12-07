import hashlib

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from App.models import *
# Create your views here.



def load_city(request):
    data = {}
    citys = CityModel.objects.all()
    citys_list = []
    for i in citys:
        citys_list.append(i.citys)
    data['citys_list'] = citys_list
    return JsonResponse(data)


def load_region(request):
    city_name = request.GET.get("city_name")
    city_object = CityModel.objects.get(citys=city_name)
    regions = city_object.regionmodel_set.all()
    regions_list = []
    for i in regions:
        regions_list.append(i.regions)

    data = {
        'regions_list': regions_list
    }

    return JsonResponse(data)


def load_user(request):
    print('load')
    data = {}
    userid = request.session.get("user_id")
    print('load id', userid)
    users = UserModel.objects.filter(pk=userid)
    if users.exists():
        user = users.first()
        data['username'] = user.username
        data['icon'] = '/static/uploadfiles/' + user.icon.url
        data['is_login'] = True
        print('okok')

    return JsonResponse(data)


def home(request):

    return render(request, "home.html")

def make_hash(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))

    return md5.hexdigest()
def register(request):
    # if request.method == 'GET':
    #     return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')

        users = UserModel.objects.filter(username=username)
        # 判断用户名是否已存在
        if users.exists():
            return HttpResponse("该用户名已存在")
        else:
            password = request.POST.get('password')
            email = request.POST.get('email')
            sex = request.POST.get('sex')
            icon = request.FILES.get('icon')

            user = UserModel()
            user.username = username
            user.password = make_hash(password)
            # user.password = password
            user.email = email
            user.icon = icon
            user.sex = sex
            user.save()
            request.session["user_id"] = user.id
            print(request.session)

            return HttpResponseRedirect('/')


def login(request):
    # if request.method == 'GET':
    #     return render(request, "login.html")
    data = {
        'is_login': False
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        print(username, pwd)

        users = UserModel.objects.filter(username=username)

        if users.exists():
            user = users.first()
            if user.password == make_hash(pwd):
            # if user.password == pwd:
                request.session['user_id'] = user.id
                data['username'] = username
                data['is_login'] = True
                print('id', user.id)

    return HttpResponseRedirect('/')


def logout(request):
    request.session.flush()
    data = {
        "out": True
    }
    return JsonResponse(data)

def blog(request):
    city = request.GET.get('city')
    cid = CityModel.objects.get(citys=city).id
    blogs = BlogModel.objects.filter(city_id = cid)
    if not blogs.exists():
        data = {
            'status': '404',
            # 'cid': cid,
            # 'uid': uid
        }
    else:
        lt = []
        blogs = blogs.all()
        for i in blogs:
            info = []
            uid = i.user_id
            users = UserModel.objects.get(id=uid)
            icons = users.icon
            username = users.username
            icon = '/static/uploadfiles/' + icons.url
            content= i.content
            info.append(uid)
            info.append(icon)
            info.append(username)
            info.append(content)
            lt.append(info)
        data = {
            'status': '200',
            'blogs': lt
        }


    return JsonResponse(data)

def save_blog(request):
    uid = request.session.get('user_id')
    city = request.GET.get('city')
    cid = CityModel.objects.get(citys=city).id
    content = request.GET.get('content')
    blg = BlogModel()
    blg.rid = 0
    blg.content = content
    blg.city_id = cid
    blg.user_id = uid
    blg.save()
    data = {
        'status':'200',
        'message':'ok'
    }
    return JsonResponse(data)



def load_house(request):
    city = request.GET.get('city')
    region = request.GET.get('region')
    min_p = request.GET.get('min_p')
    max_p = request.GET.get('max_p')
    page = request.GET.get('page')
    city_object = CityModel.objects.get(citys=city)
    city_id = city_object.id
    region_object = RegionModel.objects.filter(regions=region, city_id=city_id)
    region_object = region_object.first()
    houses_all = region_object.housemodel_set.all()

    #分页
    pagination = Paginator(houses_all.values(), 15)
    page_obj = pagination.page(page)
    # print(houses)

    data = {
        'city': city,
        'region': region,
        'min_p': min_p,
        'max_p': max_p,
        'houses': list(page_obj.object_list),
        'num': len(houses_all),
        'pagenum': len(pagination.page_range)
    }
    return JsonResponse(data)

def load_house_before(request):
    houses = HouseModel.objects.filter(id__lt=22)
    data = {
        'houses': list(houses.values())
    }
    return JsonResponse(data)

def load_house_info(request):
    houseid = request.GET.get('houseid')
    print(houseid)
    house = HouseModel.objects.filter(pk=houseid)

    print(list(house.values()))
    data = {
        'house': list(house.values())
    }
    return JsonResponse(data)


def test(request):
    htest = HouseModel.objects.filter(id__lt=20)

    pagination = Paginator(htest.values(), 4)
    page = pagination.page(2)
    print(len(pagination.page_range))
    data = {
        'data': list(page.object_list),  # 当前页的数据(列表)
        # 'page_range': pagination.page_range,  # 页码范围
        # 'page': page
    }
    return JsonResponse(data)


def hello(request):
    return JsonResponse({'result': 200, 'msg': '连接成功'})


def registerPage(request):
    return render_to_response("register_test.html")


