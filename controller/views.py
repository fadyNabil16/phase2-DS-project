from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .user import *
import json


@csrf_exempt
def Login(req):
    global user_db
    req = json.loads(req.body)
    email = req['email']
    password = req['password']
    user = User(email, password, "1")
    data = user.enter_app()
    if data is not False:
        user_db.append(user)
        response = {
            'data': data,
            'user': len(user_db)-1
        }
    else:
        response = {
            'data': data,
        }
    return JsonResponse(response, safe=False)


@csrf_exempt
def Signup(req):
    global user_db
    req = json.loads(req.body)
    email = req['email']
    password = req['password']
    name = req['name']
    region = req['region']
    store = req['store']
    user = User(email, password, "0", name, region, store)
    data = user.enter_app()
    user_db.append(user)
    response = {
        'data': data,
        'user': len(user_db)-1
    }
    return JsonResponse(response, safe=False)


@csrf_exempt
def Cash(req):
    req = json.loads(req.body)
    id = req['id']
    user_len = req['user']
    user_len = user_db[user_len]
    data = user_len.add_cash(0, id)
    items = user_len.user_items(id)
    response = {
        'money': data[0],
        'items': items
    }
    return JsonResponse(response, safe=False)


@csrf_exempt
def AddCash(req):
    req = json.loads(req.body)
    id = req['id']
    user_len = req['user']
    amount = req['amount']
    user_len = user_db[user_len]
    data = user_len.add_cash(amount, id)
    response = {
        'money': data[0],
    }
    return JsonResponse(response, safe=False)


@csrf_exempt
def EditItem(req):
    req = json.loads(req.body)
    id = req['id']
    user_len = req['user']
    list = req['list']
    lis = req['lis']
    rowid = req['rowid']
    user_len = user_db[user_len]
    user_len.item_in_store("edit", list, lis, rowid)
    response = {
    }
    return JsonResponse(response)


@csrf_exempt
def DeleteItem(req):
    req = json.loads(req.body)
    id = req['id']
    user_len = req['user']
    rowid = req['rowid']
    user_len = user_db[user_len]
    user_len.item_in_store("delete", id, rowid)
    response = {
    }
    return JsonResponse(response)


@csrf_exempt
def Search(req):
    req = json.loads(req.body)
    id = req['id']
    user_len = req['user']
    search_key = req['search_key']
    user_len = user_db[user_len]
    data = user_len.search(id, search_key)
    response = {
        'data': data
    }
    return JsonResponse(response, safe=False)


@csrf_exempt
def History(req):
    req = json.loads(req.body)
    id = req['id']
    user_len = req['user']
    user_len = user_db[user_len]
    buy, sell = user_len.history(id)
    response = {
        'buy': buy,
        'sell': sell,
    }
    return JsonResponse(response, safe=False)


@csrf_exempt
def BuyItem(req):
    req = json.loads(req.body)
    id = req['id']
    quantity = req['quantity']
    user_len = req['user']
    rowid = req['rowid']
    user_len = user_db[user_len]
    user_len.buy_item(id, rowid, quantity)
    response = {
    }
    return JsonResponse(response)


@csrf_exempt
def AddItem(req):
    req = json.loads(req.body)
    id = req['id']
    user_len = req['user']
    name = req['name']
    brand = req['brand']
    price = req['price']
    quantity = req['quantity']
    url = req['url']
    user_len = user_db[user_len]
    user_len.item_in_store("add", name, url, brand, price, quantity, id)
    response = {
    }
    return JsonResponse(response)


@csrf_exempt
def Help(req):
    req = json.loads(req.body)
    id = req['id']
    user_len = req['user']
    name = req['name']
    rowid = req['rowid']
    user_len = user_db[user_len]
    user_len.want_to_sell(id, name, rowid)
    response = {
    }
    return JsonResponse(response)


@csrf_exempt
def AllItems(req):
    req = json.loads(req.body)
    id = req['id']
    user_len = req['user']
    user_len = user_db[user_len]
    data = user_len.get_all_items(id)
    response = {
        'data': data
    }
    return JsonResponse(response, safe=False)


user_db = []
