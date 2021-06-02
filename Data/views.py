import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from Data.models import Content1, Weibo

def get_map_data(request):
    locs = Weibo.objects.values('loc')
    loc_dict = {}
    for i in locs:
        loc = i['loc'].split(" ")[0]
        if len(loc) > 3:
            loc_dict['其他'] += 1
        else:
            if loc in loc_dict.keys():
                loc_dict[loc] += 1
            else:
                loc_dict[loc] = 1
    data = []
    for key in loc_dict.keys():
        i = {}
        i['name'] = key
        i['value'] = loc_dict[key]
        data.append(i)
    return HttpResponse(json.dumps(data))
def index(request):
    return render(request=request, template_name='page2.html')
def get_sex_ratio(request):
    sexs = Weibo.objects.values('sex')
    sex_dict = {}
    for i in sexs:
        sex = i['sex']
        if sex in sex_dict.keys():
            sex_dict[sex] += 1
        else:
            sex_dict[sex] = 1
    m = {}
    m['name'] = '男生比例'
    m['value'] = sex_dict['m']
    f = {}
    f['name'] = '女生比例'
    f['value'] = sex_dict['f']
    l = [m, f]
    return HttpResponse(json.dumps(l))
def get_send_date(request):
    send_dates = Content1.objects.values('creates')
    send_date_dict = {}
    for i in send_dates:
        if i['creates'] in send_date_dict.keys():
            send_date_dict[i['creates']] += 1
        else:
            send_date_dict[i['creates']] = 1
    l = [list(send_date_dict.keys()), list(send_date_dict.values())]
    return HttpResponse(l)
def get_weibo_source(request):
    source_data = Content1.objects.values('source')
    phones = []
    for i in source_data:
        phones.append(i['source'])
    allPhones = []
    iphone = {}
    iphone['name'] = '苹果'
    iphone['value'] = 0
    huawei = {}
    huawei['name'] = '华为'
    huawei['value'] = 0
    xiaomi = {}
    xiaomi['name'] = '小米'
    xiaomi['value'] = 0
    vivo = {}
    vivo['name'] = 'vivo'
    vivo['value'] = 0
    oppo = {}
    oppo['name'] = 'oppo'
    oppo['value'] = 0
    samsung = {}
    samsung['name'] = '三星'
    samsung['value'] = 0
    meizu = {}
    meizu['name'] = '魅族'
    meizu['value'] = 0
    android = {}
    android['name'] = "其他安卓客户端"
    android['value'] = 0
    meitu = {}
    meitu['name'] = '美图'
    meitu['value'] = 0
    lenveo = {}
    lenveo['name'] = '联想'
    lenveo['value'] = 0
    oneplus = {}
    oneplus['name'] = '一加'
    oneplus['value'] = 0
    nubia = {}
    nubia['name'] = '努比亚'
    nubia['value'] = 0
    nokia = {}
    nokia['name'] = '诺基亚'
    nokia['value'] = 0
    browser = {}
    browser['name'] = '浏览器'
    browser['value'] = 0
    for l in phones:
        if l.__contains__("超话"):
            pass
        elif l.__contains__("iPhone") or l.__contains__("iPad") or l.__contains__('iOS'):
            iphone['value'] += 1
        elif l.__contains__("华为") or l.__contains__("荣耀") or l.__contains__("HUAWEI") or l.__contains__(
                'nova') or l.__contains__('麦芒'):
            huawei['value'] += 1
        elif l.__contains__("小米") or l.__contains__('红米') or l.__contains__('Redmi'):
            xiaomi['value'] += 1
        elif l.__contains__("vivo"):
            vivo['value'] += 1
        elif l.__contains__('oppo') or l.__contains__('OPPO'):
            oppo['value'] += 1
        elif l.__contains__('Samsung') or l.__contains__('三星'):
            samsung['value'] += 1
        elif l.__contains__('魅蓝') or l.__contains__('魅族'):
            meizu['value'] += 1
        elif l.__contains__('美图'):
            meitu['value'] += 1
        elif l.__contains__('OnePlus'):
            oneplus['value'] += 1
        elif l.__contains__('联想'):
            lenveo['value'] += 1
        elif l.__contains__('努比亚'):
            nubia['value'] += 1
        elif l.__contains__('诺基亚'):
            nokia['value'] += 1
        elif l.__contains__('浏览器'):
            browser['value'] += 1
        elif l.__contains__("android") or l.__contains__('Android'):
            android['value'] += 1
    allPhones.append(iphone)
    allPhones.append(huawei)
    allPhones.append(xiaomi)
    allPhones.append(vivo)
    allPhones.append(oppo)
    allPhones.append(samsung)
    allPhones.append(meitu)
    allPhones.append(meizu)
    allPhones.append(oneplus)
    allPhones.append(lenveo)
    allPhones.append(nubia)
    allPhones.append(nokia)
    allPhones.append(browser)
    allPhones.append(android)
    name = []
    for i in allPhones:
        name.append(i.get('name'))
    return HttpResponse([name, allPhones])
def get_data_info(request):
    up_num = Weibo.objects.count()
    weibo_num = Content1.objects.count()
    l = [up_num, weibo_num]
    return HttpResponse(json.dumps(l))